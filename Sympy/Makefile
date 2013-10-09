base = Sympy
all: $(base).pdf 

.PHONY: $(base).pdf
$(base).pdf: $(base).rst 
	rst2pdf --stylesheet-path=../styles -b 1 -s slides -s manni $<

.PHONY: clean
clean:
	-rm -f $(base).pdf *.pyc *.pyo
