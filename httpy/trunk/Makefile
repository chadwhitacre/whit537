VERSION=1.0

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
# Replace ~~VERSION~~ with the version number in all files except this one and
# hidden svn files.
	find . -type f \
	       \! -regex '.*/.svn.*' \
	       \! -regex '\./Makefile' \
	       -exec sed -e 's/~~VERSION~~/$(VERSION)/g' -i '' {} \;

dist: version clean
	mkdir dist
	mkdir dist/httpy-${VERSION}
	cp -r README \
	      src \
	      setup.py \
	      dist/httpy-${VERSION}

	make -C doc/tex all clean
	mkdir dist/httpy-${VERSION}/doc
	cp -r doc/html \
	      doc/httpy-${VERSION}.pdf \
	      doc/HISTORY \
	      dist/httpy-${VERSION}/doc

	tar --directory dist -zcf dist/httpy-${VERSION}.tgz httpy-${VERSION}
	tar --directory dist -jcf dist/httpy-${VERSION}.tbz httpy-${VERSION}

# ZIP archive gets different line endings
	svneol clean -w dist/httpy-${VERSION}
	cd dist && zip -9rq httpy-${VERSION}.zip httpy-${VERSION}
#	rm -rf dist/httpy-${VERSION}
