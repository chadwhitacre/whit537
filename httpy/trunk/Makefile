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

version:
    find . -type f -exec sed -E 's/~~VERSION~~//g'

dist: version clean
	mkdir dist
	mkdir dist/httpy-${version}
	cp -r README \
	      src \
	      setup.py \
	      dist/httpy-${version}

	make -C doc/tex all clean
	mkdir dist/httpy-${version}/doc
	cp -r doc/html \
	      doc/httpy-${version}.pdf \
	      doc/HISTORY \
	      dist/httpy-${version}/doc

	tar --directory dist -zcf dist/httpy-${version}.tgz httpy-${version}
	tar --directory dist -jcf dist/httpy-${version}.tbz httpy-${version}

# ZIP archive gets different line endings
	svneol clean -w dist/httpy-${version}
	cd dist && zip -9rq httpy-${version}.zip httpy-${version}
#	rm -rf dist/httpy-${version}