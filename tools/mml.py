"""Print the MathML attached to a PDF: every stream that inflates to something starting
with <math. Usage: mml.py file.pdf [--count]"""
import re, sys, zlib
d = open(sys.argv[1], 'rb').read()
out = []
for m in re.finditer(rb'stream\r?\n', d):
    e = d.find(b'endstream', m.end())
    raw = d[m.end():e]
    for cand in (raw,):
        try:
            data = zlib.decompress(cand)
        except Exception:
            data = cand
        if data.lstrip().startswith(b'<math'):
            out.append(data.decode('utf-8', 'replace').strip())
if '--count' in sys.argv:
    print(len(out), 'MathML files,', sum(len(o) for o in out), 'bytes')
else:
    for o in out:
        print(o); print()
