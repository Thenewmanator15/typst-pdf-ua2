"""bench.py DOC ROUNDS [EXTRA_ARGS...]: with TYPST_BASE and TYPST_PROTOTYPE set to the two
binaries, times `typst compile` for an unmodified Typst and
the PDF/UA-2 prototype, both built from the same commit with the same compiler.

For each build and PDF standard it reports the median and best wall time over ROUNDS runs
(the builds and modes are interleaved, so that drift affects them alike), the peak working
set of the process, and the size of the PDF. Windows only: the peak is read with
GetProcessMemoryInfo."""
import ctypes
import ctypes.wintypes as wt
import os
import statistics
import subprocess
import sys
import time

# The two Typst binaries to compare: an unmodified build and the prototype.
BUILDS = {
    'base': os.environ.get('TYPST_BASE', 'typst-base'),
    'prototype': os.environ.get('TYPST_PROTOTYPE', 'typst'),
}
MODES = {
    'base': ['1.7', 'ua-1', '2.0'],
    'prototype': ['1.7', 'ua-1', '2.0', 'ua-2'],
}


class Counters(ctypes.Structure):
    _fields_ = [('cb', wt.DWORD), ('PageFaultCount', wt.DWORD),
                ('PeakWorkingSetSize', ctypes.c_size_t), ('WorkingSetSize', ctypes.c_size_t),
                ('QuotaPeakPagedPoolUsage', ctypes.c_size_t), ('QuotaPagedPoolUsage', ctypes.c_size_t),
                ('QuotaPeakNonPagedPoolUsage', ctypes.c_size_t), ('QuotaNonPagedPoolUsage', ctypes.c_size_t),
                ('PagefileUsage', ctypes.c_size_t), ('PeakPagefileUsage', ctypes.c_size_t)]


psapi = ctypes.WinDLL('psapi')
psapi.GetProcessMemoryInfo.argtypes = [wt.HANDLE, ctypes.POINTER(Counters), wt.DWORD]


def run(exe, mode, doc, out, extra):
    start = time.perf_counter()
    p = subprocess.Popen([exe, 'compile', '--pdf-standard', mode, *extra, doc, out],
                         stdout=subprocess.DEVNULL, stderr=subprocess.PIPE)
    _, err = p.communicate()
    elapsed = time.perf_counter() - start
    c = Counters()
    c.cb = ctypes.sizeof(c)
    psapi.GetProcessMemoryInfo(int(p._handle), ctypes.byref(c), c.cb)
    if p.returncode != 0:
        raise SystemExit(f'{exe} {mode} failed:\n{err.decode("utf-8", "replace")[:600]}')
    return elapsed, c.PeakWorkingSetSize, os.path.getsize(out)


doc, rounds, extra = sys.argv[1], int(sys.argv[2]), sys.argv[3:]
cases = [(b, m) for b in BUILDS for m in MODES[b]]
results = {case: [] for case in cases}
for case in cases:  # one run each to warm the file cache, not counted
    run(BUILDS[case[0]], case[1], doc, f'out-{case[0]}-{case[1]}.pdf', extra)
for _ in range(rounds):
    for case in cases:
        results[case].append(run(BUILDS[case[0]], case[1], doc, f'out-{case[0]}-{case[1]}.pdf', extra))

print(f'{"build":<10}{"standard":<9}{"median":>10}{"best":>10}{"peak memory":>14}{"PDF size":>12}')
for (build, mode), runs in results.items():
    times = [r[0] for r in runs]
    print(f'{build:<10}{mode:<9}{statistics.median(times):>8.2f} s{min(times):>8.2f} s'
          f'{statistics.median(r[1] for r in runs) / 2**20:>11.0f} MB{runs[-1][2] / 1024:>9.0f} KB')
