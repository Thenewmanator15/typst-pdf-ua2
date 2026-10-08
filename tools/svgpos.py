"""svgpos.py DIR_A DIR_B: compares the SVG pages of two builds by where every glyph, image
and path ends up on the page, after working out the nested transforms. Grouping is ignored,
so two builds that draw the same things in the same places compare equal even if one wraps
them in an extra group.

Prints the largest difference in position, in points, and any page whose drawn items differ.
"""
import os
import re
import sys

TAG = re.compile(r'<(/?)(\w+)([^>]*?)(/?)>')
NUM = r'(-?\d+(?:\.\d+)?(?:e-?\d+)?)'


def matrix(attr):
    """The transform attribute as (a, b, c, d, e, f)."""
    m = (1.0, 0.0, 0.0, 1.0, 0.0, 0.0)
    for name, args in re.findall(r'(\w+)\(([^)]*)\)', attr):
        v = [float(x) for x in re.findall(NUM, args)]
        if name == 'translate':
            t = (1.0, 0.0, 0.0, 1.0, v[0], v[1] if len(v) > 1 else 0.0)
        elif name == 'matrix':
            t = tuple(v)
        elif name == 'scale':
            t = (v[0], 0.0, 0.0, v[1] if len(v) > 1 else v[0], 0.0, 0.0)
        else:
            raise ValueError(name)
        m = mul(m, t)
    return m


def mul(m, t):
    a, b, c, d, e, f = m
    a2, b2, c2, d2, e2, f2 = t
    return (a * a2 + c * b2, b * a2 + d * b2, a * c2 + c * d2, b * c2 + d * d2,
            a * e2 + c * f2 + e, b * e2 + d * f2 + f)


def items(path):
    text = open(path, encoding='utf-8').read()
    # Typst puts the glyph definitions in <defs> blocks, which are not drawn.
    body = re.sub(r'<defs.*?</defs>', '', text, flags=re.S)
    stack = [(1.0, 0.0, 0.0, 1.0, 0.0, 0.0)]
    out = []
    for close, name, attrs, selfclose in TAG.findall(body):
        if close:
            if name == 'g':
                stack.pop()
            continue
        tr = re.search(r'transform="([^"]*)"', attrs)
        m = mul(stack[-1], matrix(tr.group(1))) if tr else stack[-1]
        if name == 'g' and not selfclose:
            stack.append(m)
            continue
        if name in ('use', 'image', 'path', 'rect'):
            x = float((re.search(r'\bx="' + NUM + '"', attrs) or [0, 0])[1])
            y = float((re.search(r'\by="' + NUM + '"', attrs) or [0, 0])[1])
            a, b, c, d, e, f = m
            ref = re.search(r'href="([^"]*)"', attrs)
            shape = re.search(r'\bd="([^"]*)"', attrs)
            key = (name, ref.group(1) if ref else '', shape.group(1) if shape else '',
                   round(a, 6), round(b, 6), round(c, 6), round(d, 6))
            out.append((key, a * x + c * y + e, b * x + d * y + f))
    return out


a_dir, b_dir = sys.argv[1], sys.argv[2]
worst = 0.0
pages = 0
count = 0
bad = []
for name in sorted(os.listdir(a_dir)):
    if not name.endswith('.svg'):
        continue
    pages += 1
    ia, ib = items(os.path.join(a_dir, name)), items(os.path.join(b_dir, name))
    if [k for k, _, _ in ia] != [k for k, _, _ in ib]:
        bad.append(name)
        continue
    count += len(ia)
    for (_, xa, ya), (_, xb, yb) in zip(ia, ib):
        worst = max(worst, abs(xa - xb), abs(ya - yb))
print(f'pages compared: {pages}; items compared: {count}; pages whose drawn items differ: {len(bad)} {bad[:5]}')
print(f'largest difference in position: {worst:.9f} pt')
