from distutils.core import setup


classifiers = [
    'Development Status :: 5 - Production/Stable'
  , 'Environment :: No Input/Output (Daemon)'
  , 'Intended Audience :: Developers'
  , 'License :: OSI Approved :: Python Software Foundation License'
  , 'Natural Language :: English'
  , 'Operating System :: MacOS :: MacOS X'
  , 'Operating System :: POSIX'
  , 'Operating System :: Unix'
  , 'Programming Language :: Python'
  , 'Topic :: Software Development :: Libraries :: Python Modules'
   ]


setup( name='daemon.py'
     , version='1.0'
     , package_dir = {'':'src'}
     , py_modules=['daemon']
     , description = ( "daemon.py is a Python implementation of the standard "
                     + "UNIX double-fork technique."
                      )
     , author = 'Chad Whitacre'
     , author_email = 'chad@zetaweb.com'
     , url = 'http://www.zetadev.com/software/daemon.py/'
     , classifiers = classifiers
      )
