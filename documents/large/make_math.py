"""make_math.py EQUATIONS OUT: writes a Typst document that is mostly mathematics, to
measure what making MathML for every equation costs. Each paragraph has three inline
equations and is followed by a display equation. The equations differ from one another, so
that none of the MathML can be shared. Each has alternative text, so that the document
can also be exported as PDF/UA-1."""
import sys

n = int(sys.argv[1])
out = [
    '#set document(title: "Mathematics benchmark")',
    '#set text(lang: "en")',
    '#set heading(numbering: "1.1")',
    '#let eq(alt, body) = math.equation(alt: alt, body)',
    '#let deq(alt, body) = math.equation(block: true, alt: alt, body)',
    '',
]
i = 0
while i < n:
    if i % 200 == 0:
        out.append(f'= Part {i // 200 + 1}')
    k = i + 1
    out.append(
        f'Let #eq("x {k}", $x_{k} in RR$) and #eq("a sum", $sum_(j=1)^{k} j = ({k} dot {k + 1})/2$), '
        f'so that #eq("a bound", $abs(f(x_{k})) <= sqrt({k}) + alpha^{k % 9 + 2}$) holds. #lorem(20)'
    )
    out.append(
        f'#deq("an integral", $ integral_0^{k} (x^{k % 7 + 2} + {k}) / (1 + x^2) dif x '
        f'= lim_(n -> oo) sum_(i=1)^n mat(a_{k}, b; c, d_{k % 5}) vec(i, n) $)'
    )
    out.append('')
    i += 4
open(sys.argv[2], 'w', encoding='utf-8', newline='\n').write('\n'.join(out) + '\n')
