from distutils.core import setup


classifiers = [
    'Development Status :: 3 - Alpha'
  , 'Intended Audience :: Developers'
  , 'License :: OSI Approved :: BSD License'
  , 'Natural Language :: English'
  , 'Operating System :: MacOS :: MacOS X'
  , 'Operating System :: Microsoft :: Windows'
  , 'Operating System :: POSIX'
  , 'Operating System :: Unix'
  , 'Programming Language :: Python'
  , 'Topic :: Software Development :: Libraries :: Python Modules'
   ]


setup( name='mode.py'
     , version='1.0a1'
     , package_dir = {'':'src'}
     , py_modules=['mode']
     , description = ( 'mode.py models the life-cycle of an application as a '
                     + 'series of four modes.'
                      )
     , author = 'Chad Whitacre'
     , author_email = 'chad@zetaweb.com'
     , url = 'http://www.zetadev.com/software/mode.py/'
     , classifiers = classifiers
      )
