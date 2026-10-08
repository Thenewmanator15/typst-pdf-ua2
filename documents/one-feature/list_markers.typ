// Bullet and numbered lists whose labels differ by level. ListNumbering should say which.
#set document(title: "List markers")
#set text(lang: "en")
- a solid dot
  - a triangle
    - a dash

#set enum(numbering: "1.a.i.")
+ a number
  + a letter
    + a roman numeral

#set list(marker: [▪])
- a square
