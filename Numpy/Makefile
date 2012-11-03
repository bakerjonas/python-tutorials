pyfiles = array.py linalg.py operators.py random1.py random2.py 

all: Numpy.pdf

Numpy.pdf: Numpy.rst $(pyfiles)
	rst2pdf --stylesheet-path=../styles -b 1 -s slides -s murphy $<

.PHONY: Notebook.py
Notebook.py: 
	@echo "# -*- coding: utf-8 -*-" > $@
	@echo "# <nbformat>3.0</nbformat>" >> $@
	for i in $(pyfiles); do echo "\n# <codecell>" >> $@; cat $$i >> $@; done

.PHONY: clean
clean:
	-rm -f Numpy.pdf Notebook.py *.pyc *.pyo
