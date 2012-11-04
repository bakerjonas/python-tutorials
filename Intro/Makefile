pyfiles = nums.py vars.py strings.py string_ops.py string_methods.py \
		  lists.py tuples.py dicts.py ifelse.py \
		  while.py for.py looptricks.py import.py \
		  readfile.py writefile.py funcdef.py \
		  class.py object.py dynamic.py 

all: Intro.pdf 

.PHONY: Intro.pdf
Intro.pdf: Intro.rst 
	rst2pdf --stylesheet-path=../styles -b 1 -s slides -s manni $<

.PHONY: Notebook.py
Notebook.py: 
	@echo "# -*- coding: utf-8 -*-" > $@
	@echo "# <nbformat>3.0</nbformat>" >> $@
	for i in $(pyfiles); do echo "\n# <codecell>" >> $@; cat $$i >> $@; done

.PHONY: clean
clean:
	-rm -f Intro.pdf Notebook.py *.pyc *.pyo
