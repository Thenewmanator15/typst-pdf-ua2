"""treedump.py FILE: prints the structure tree of a PDF written with --pretty (structure
elements not in object streams), with the marked-content ids of each element in order."""
import re, sys
d = open(sys.argv[1], 'rb').read()
objs = {int(m.group(1)): m.group(2).decode('latin-1')
        for m in re.finditer(rb'(\d+) 0 obj\r?\n(.*?)\r?\nendobj', d, re.S)}
el = {n: b for n, b in objs.items() if '/Type /StructElem' in b}


def kids(b):
    k = re.search(r'/K (\[.*\]|\d+ 0 R|\d+)\s*(?:/|>>|$)', b, re.S)
    if not k:
        return []
    body = re.sub(r'<<.*?>>', ' annot ', k.group(1), flags=re.S)
    return re.findall(r'(\d+) 0 R|(?<![\d.])(\d+)(?![\d.]| 0 R)|(annot)', body)


def show(n, depth):
    b = el[n]
    name = re.search(r'/S /(\w+)', b).group(1)
    extra = ''
    if '/Subtype /LineNum' in b:
        extra = ' (LineNum)'
    if '/role' in b:
        extra = ' (' + re.search(r'/role /([\w-]+)', b).group(1) + ')'
    line = '  ' * depth + name + extra
    leaves = []
    children = []
    for ref, mcid, annot in kids(b):
        if ref and int(ref) in el:
            children.append(('el', int(ref)))
        elif mcid:
            children.append(('mc', mcid))
        elif annot:
            children.append(('mc', 'annot'))
    if all(kind == 'mc' for kind, _ in children):
        print(line + (' [' + ' '.join(v for _, v in children) + ']' if children else ''))
        return
    print(line)
    for kind, v in children:
        if kind == 'el':
            show(v, depth + 1)
        else:
            print('  ' * (depth + 1) + '[' + str(v) + ']')


root = [n for n, b in el.items() if re.search(r'/S /Document', b)][0]
show(root, 0)
