pyfiles = array.py linalg.py operators.py random1.py random2.py 

all: Numpy.pdf

Numpy.pdf: Numpy.rst $(pyfiles)
	rst2pdf --stylesheet-path=../styles -b 1 -s slides -s murphy $<
