pyfiles = participants.py

all: textparsing.pdf 

.PHONY: textparsing.pdf
textparsing.pdf: textparsing.rst 
	rst2pdf --stylesheet-path=../styles -b 1 -s slides -s manni $<

.PHONY: Notebook.py
Notebook.py: 
	@echo "# -*- coding: utf-8 -*-" > $@
	@echo "# <nbformat>3.0</nbformat>" >> $@
	for i in $(pyfiles); do echo "\n# <codecell>" >> $@; cat $$i >> $@; done

.PHONY: clean
clean:
	-rm -f textparsing.pdf Notebook.py *.pyc *.pyo
