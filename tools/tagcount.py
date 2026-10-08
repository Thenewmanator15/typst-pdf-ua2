"""tagcount.py FILE: counts the structure types (/S values) in a PDF, including those in
object streams."""
import re, sys, zlib, collections
d = open(sys.argv[1], 'rb').read()
parts = [d]
for m in re.finditer(rb'stream\r?\n', d):
    e = d.find(b'endstream', m.end())
    try:
        parts.append(zlib.decompress(d[m.end():e]))
    except Exception:
        pass
c = collections.Counter()
for p in parts:
    for t in re.findall(rb'/S\s*/([A-Za-z0-9]+)', p):
        c[t.decode()] += 1
print(' '.join(f'{k}:{v}' for k, v in sorted(c.items())))
