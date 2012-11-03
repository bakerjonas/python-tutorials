pyfiles = class.py dynamic.py for.py funcdef.py ifelse.py import.py \
object.py readfile.py silly.py vars.py while.py writefile.py 

all: Intro.pdf

Intro.pdf: Intro.rst $(pyfiles)
	rst2pdf --stylesheet-path=../styles -b 1 -s slides -s murphy $<

