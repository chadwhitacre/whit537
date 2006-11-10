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
  , 'Topic :: Internet :: WWW/HTTP'
  , 'Topic :: Internet :: WWW/HTTP :: WSGI'
  , 'Topic :: Internet :: WWW/HTTP :: WSGI :: Middleware'
  , 'Topic :: Software Development :: Libraries :: Python Modules'
   ]


setup( name='httpy'
     , version='~~VERSION~~'
     , package_dir = {'':'src'}
     , py_modules=['httpy']
     , description = "httpy smooths out a few of WSGI's most glaring warts."
     , author = 'Chad Whitacre'
     , author_email = 'chad@zetaweb.com'
     , url = 'http://www.zetadev.com/software/httpy/'
     , classifiers = classifiers
      )
