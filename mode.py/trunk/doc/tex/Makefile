# Makefile to create documentation using the Python LaTeX system.

VERSION=1.0
PYTHON_SRC = /home/whit537/python/2.4.3/src
MKHOWTO    = $(PYTHON_SRC)/Doc/tools/mkhowto \
				--iconserver icons \
				--link 1 \
				--split 1 \
				--favicon icons/zeta.ico \
				--dir ./html \
				--logging \
				--up-link "http://www.zetadev.com/software/mode.py/" \
				--up-title "mode.py homepage" \
				--address "<a href=\"http://www.zetadev.com/software/mode.py/\">mode.py is Zeta software</a>. It is copyright &copy; 2006 by Chad Whitacre, and is offered under the new BSD license." \
#				--style style.css


default: html

html: clean
	$(MKHOWTO) mode.tex
	cp -r ../icons ./html/
	rm -rf ./html/icons/.svn
	rm -rf ../html && mv ./html ../

pdf:
	$(PYTHON_SRC)/Doc/tools/mkhowto --pdf mode.tex
	mv mode.pdf ../mode.py-$(VERSION).pdf

clean:
	rm -rf *~ *.aux *.idx *.ilg *.ind *.log *.toc *.bkm *.syn \
		   *.pla *.eps *.pdf *.ps *.lof *.l2h *.tex2 *.dvi html ../*.pdf

all: html pdf clean