// A numbered equation that is also given alternative text. Its number still has to be a
// label, although the other tags inside a described element are left out.
#set document(title: "Numbered equation with alt text")
#set text(lang: "en")
#set math.equation(numbering: "(1)")
#math.equation(block: true, alt: "a squared plus b squared equals c squared", $ a^2 + b^2 = c^2 $) <eq>
$ x = 1 $
See @eq.
