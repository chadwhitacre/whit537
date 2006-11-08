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
	mkdir dist/daemon.py-${version}
	cp -r README \
	      src \
	      setup.py \
	      dist/daemon.py-${version}

	make -C doc/tex all clean
	mkdir dist/daemon.py-${version}/doc
	cp -r doc/html \
	      doc/daemon.py-${version}.pdf \
	      doc/HISTORY \
	      dist/daemon.py-${version}/doc

	tar --directory dist -zcf dist/daemon.py-${version}.tgz daemon.py-${version}
	tar --directory dist -jcf dist/daemon.py-${version}.tbz daemon.py-${version}

# ZIP archive gets different line endings
	svneol clean -w dist/daemon.py-${version}
	cd dist && zip -9rq daemon.py-${version}.zip daemon.py-${version}
#	rm -rf dist/daemon.py-${version}