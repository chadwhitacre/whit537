version=1.0

clean:
# remove all of the cruft that gets auto-generated on doc/install/release
	rm -rf build
	rm -rf dist
	find . -name \*.pyc | xargs rm
	make -C doc/tex clean


# Target for building a distribution
# ==================================
# note the dependency on svneol: http://www.zetadev.com/svn/public/svneol/

dist: clean
	mkdir dist
	mkdir dist/mode.py-${version}
	cp -r README \
	      src \
	      setup.py \
	      dist/mode.py-${version}

	make -C doc/tex all clean
	mkdir dist/mode.py-${version}/doc
	cp -r doc/html \
	      doc/mode.py-${version}.pdf \
	      doc/HISTORY \
	      dist/mode.py-${version}/doc

	tar --directory dist -zcf dist/mode.py-${version}.tgz mode.py-${version}
	tar --directory dist -jcf dist/mode.py-${version}.tbz mode.py-${version}

# ZIP archive gets different line endings
	svneol clean -w dist/mode.py-${version}
	cd dist && zip -9rq mode.py-${version}.zip mode.py-${version}
#	rm -rf dist/mode.py-${version}