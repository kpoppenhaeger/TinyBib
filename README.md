TinyBib
=======

Make a tiny references section using latex/bibtex.


Say you're about to write some epic observing proposal. Or anything else where you have a strict page limit.

Say you want the reader to see that you have done awesome stuff, so you cite everything with author names: Poppenhaeger et al. (2013).

This will use quite some space in the proposal text, which means you want to save space in the references section. So I've made a bibliography style file (bibshort.bst) and a python script (TinyBib.py) to hack the output from that file in order to get a really small references section.

Example how to use it:

Run pdflatex (or latex) for the example.tex file:

pdflatex example

Then run bibtex:

bibtex example

Then run the python script:

python TinyBib.py example.bbl

Then run pdflatex/latex twice to get the references right:

pdflatex example
pdflatex example

And that's it.

