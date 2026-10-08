// Every heading level the template styles, numbered and not, short and wrapping,
// in the main body and in the appendices.
#import "@preview/casson-uom-thesis:0.1.2": *

#show: uom-thesis.with(
  title: "A test of the heading styles",
  author: "A. Tester",
  faculty: "Science and Engineering",
  school: "School of Engineering",
  departmentordivision: "Department of Electrical and Electronic Engineering",
  abstract: [Abstract goes here],
  publications: [Publications go here.],
  acknowledgements: [Acknowledgements go here.],
  year: "2026",
  font: "times",
  fontsize: 11pt,
)

= Introduction
#lorem(40)

== A section
#lorem(40)

=== A sub-section
#lorem(40)

==== A level four heading
#lorem(40)

===== A level five heading
#lorem(40)

====== A level six heading
#lorem(40)

== A section with a title that is long enough to run on to a second line of the page when it is set in the larger size
#lorem(30)

=== A sub-section with a title that is long enough to run on to a second line of the page when it is set in the larger size, which takes some words
#lorem(30)

= A chapter with a title that is long enough to run on to a second line
#lorem(30)

#heading(numbering: none)[An unnumbered chapter]
#lorem(30)

#heading(level: 2, numbering: none)[An unnumbered section]
#lorem(30)

= Headings one after another
== Straight into a section
=== And a sub-section
#lorem(30)

Text before a heading at the foot of a paragraph.
== A section after text
Text straight after.

#show: uom-appendix
= First appendix
#lorem(30)

== A section in the appendix
#lorem(30)

=== A sub-section in the appendix
#lorem(30)

#heading(level: 2, numbering: none)[An unnumbered section in the appendix]
#lorem(30)

= A second appendix with a title that is long enough to run on to a second line
== Straight into a section
#lorem(30)
