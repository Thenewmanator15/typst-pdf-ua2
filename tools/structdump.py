"""structdump.py FILE [TYPE ...]: prints the path from the root for each structure element
of the given types in a PDF written by krilla (objects not in object streams)."""
import re, sys
data = open(sys.argv[1], 'rb').read().decode('latin-1')
objs = {int(m.group(1)): m.group(2) for m in re.finditer(r'(?:^|\n)(\d+) 0 obj\s*(.*?)\s*endobj', data, re.S)}
def typ(n):
    d = objs.get(n, '')
    m = re.search(r'/S\s*/(\w+)', d)
    return m.group(1) if m and '/StructElem' in d else None
def parent(n):
    m = re.search(r'/P\s+(\d+) 0 R', objs.get(n, ''))
    return int(m.group(1)) if m else None
def kids(n):
    m = re.search(r'/K\s*\[(.*?)\]', objs.get(n, ''), re.S)
    return [typ(int(x)) or '?' for x in re.findall(r'(\d+) 0 R', m.group(1))] if m else []
want = set(sys.argv[2:])
for n in sorted(objs):
    t = typ(n)
    if t in want:
        path, p = [t], parent(n)
        while p and typ(p):
            path.append(typ(p)); p = parent(p)
        par = parent(n)
        print(' > '.join(reversed(path)), '| siblings:', kids(par)[:12])
