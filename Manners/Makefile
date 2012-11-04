pyfiles = 
all: Devel.pdf 

.PHONY: Devel.pdf
Devel.pdf: Devel.rst 
	rst2pdf --stylesheet-path=../styles -b 1 -s slides -s manni $<

.PHONY: clean
clean:
	-rm -f Devel.pdf Notebook.py *.pyc *.pyo
