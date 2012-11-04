pyfiles = 
all: OOP.pdf 

.PHONY: OOP.pdf
OOP.pdf: OOP.rst 
	rst2pdf --stylesheet-path=../styles -b 1 -s slides -s manni $<

.PHONY: clean
clean:
	-rm -f OOP.pdf Notebook.py *.pyc *.pyo
