# Makefile to create documentation using the Python LaTeX system. Set the
# PYTHONSRC environment variable to the root of a Python source distribution.
# This file also obeys the VERSION envvar set in the root Makefile.

#VERSION=~~VERSION~~
#PYTHONSRC=/home/whit537/python/2.4.3/src
MKHOWTO    = $(PYTHONSRC)/Doc/tools/mkhowto \
				--iconserver icons \
				--split 1 \
				--link 1 \
				--favicon icons/zeta.ico \
				--dir ./html \
				--logging \
				--up-link "http://www.zetadev.com/software/httpy/" \
				--up-title "httpy homepage" \
				--address "<a href=\"http://www.zetadev.com/software/httpy/\">httpy is Zeta software</a>. It is copyright &copy; 2006 by Chad Whitacre, and is offered free of charge, warranty, and restrictions." \
#				--style style.css


default: html

html: clean
	$(MKHOWTO) httpy.tex
	cp -r ../icons ./html/
	rm -rf ./html/icons/.svn
	rm -rf ../html && mv ./html ../

pdf:
	$(PYTHONSRC)/Doc/tools/mkhowto --pdf httpy.tex
	mv httpy.pdf ../httpy-$(VERSION).pdf

clean:
	rm -rf *~ *.aux *.idx *.ilg *.ind *.log *.toc *.bkm *.syn \
		   *.pla *.eps *.pdf *.ps *.lof *.l2h *.tex2 *.dvi ../html ../*.pdf
