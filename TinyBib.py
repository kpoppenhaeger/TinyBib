# -*- coding: utf-8 -*-

# make the bibliography tiny.

# you need to use natbib, and in the preamble of your latex document, you want to have this:
#\usepackage{natbib}
#\setlength{\bibsep}{-10pt} % this avoids an empty page after your tiny bibliography.

# call this program as:
# python make_the_bib_tiny.py your_file_name_with_path.bbl

import sys
import numpy as np

print 'Compressing your bbl file:', str(sys.argv[1])
print 'Now run latex/pdflatex.'


infile = str(sys.argv[1])

with open(infile) as f:
    content = f.readlines()


minirefs = []
minibib = []

for i in np.arange(len(content)):
  if (content[i][0] != "{"):
    minirefs.append(content[i])
  else:
    minibib.append(content[i])

# first 3 lines are preamble, put into separate variable:
preamble = minirefs[0:3]

# delete those first 3 lines from minirefs:
minirefs.remove(minirefs[0])
minirefs.remove(minirefs[0])
minirefs.remove(minirefs[0])

# now put stuff together. 
# overwrite the old bbl file.
f = open(infile,'w')

# first the preamble
for line in preamble:
  f.write(line)

# then the minipage environment for the minibib
f.write('\\item\n')
f.write('\\begin{minipage}{0.5\\textwidth}\n')

# then the minibib itself
for line in minibib:
  f.write(line)

# then close the minipage environment
f.write('\\end{minipage}\n')

# then the minirefs
for line in minirefs:
  f.write(line)

# and close the file.
f.close()



