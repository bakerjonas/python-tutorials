pyfiles = class.py dynamic.py for.py funcdef.py ifelse.py import.py \
object.py readfile.py silly.py vars.py while.py writefile.py 

all: Intro.pdf 

.PHONY: Intro.pdf
Intro.pdf: Intro.rst 
	rst2pdf --stylesheet-path=../styles -b 1 -s slides -s murphy $<

.PHONY: Notebook.py
Notebook.py: 
	@echo "# -*- coding: utf-8 -*-" > $@
	@echo "# <nbformat>3.0</nbformat>" >> $@
	for i in $(pyfiles); do echo "\n# <codecell>" >> $@; cat $$i >> $@; done

.PHONY: clean
clean:
	-rm -f Intro.pdf Notebook.py *.pyc *.pyo
