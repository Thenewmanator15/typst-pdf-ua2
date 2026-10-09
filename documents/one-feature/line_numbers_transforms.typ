// Numbered lines inside moved, rotated, scaled and padded content. Each number still has
// to end up at its own line.
#set document(title: "Line numbers under transforms")
#set text(lang: "en")
#set page(width: 10cm, margin: (left: 2cm))
#set par.line(numbering: "1")
A plain first line that wraps onto a second line of this narrow page for sure.

#move(dy: 8pt)[A moved paragraph that also wraps onto a second line of the page.]

#rotate(4deg)[A slightly rotated paragraph that wraps onto a second line as well.]

#scale(90%)[A scaled paragraph that wraps onto a second line as well, like the others.]

#pad(left: 1cm)[A padded paragraph that wraps onto a second line as well, like the others.]

A last plain line.
