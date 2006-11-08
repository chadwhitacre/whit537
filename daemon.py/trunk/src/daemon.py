"""Disk And Execution MONitor (daemon) support.

Adapted from Chad J. Schroeder's recipe:

    http://aspn.activestate.com/ASPN/Cookbook/Python/Recipe/278731

The original is (c) 2005 by Chad J. Schroeder, and is used here under "the
Python license," per ASPN's notice:

    Except where otherwise noted, recipes in the Python Cookbook are published
    under the Python license <http://www.python.org/license>.

"""
import os
import resource
import sys


if (hasattr(os, "devnull")):
    DEVNULL = os.devnull
else:
    DEVNULL = "/dev/null"


def become(umask=0, workdir='/', maxfd=1024, redirect_to=DEVNULL):
    """Daemonize the current process.
    """

    # Fork the first child.
    # =====================

    try:
        pid = os.fork()
    except OSError, e:
        raise Exception, "%s [%d]" % (e.strerror, e.errno)

    if pid == 0:

        # Take over the new session and process group.
        # ============================================

        os.setsid()


        # Fork the second child.
        # ======================

        try:
            pid = os.fork()
        except OSError, e:
            raise Exception, "%s [%d]" % (e.strerror, e.errno)

        if pid != 0:

            # Exit parent of the second child (i.e., the first child).
            # ========================================================

            os._exit(0)


    else:

        # Exit parent of the first child.
        # ===============================

        os._exit(0)


    # Clean up the new process.
    # =========================
    #  - Change the current working directory and file mode creation mask.
    #  - Close all open file descriptors.
    #  - Redirect the standard I/O file descriptors to /dev/null.

    os.chdir(workdir)
    os.umask(umask)

    nofile = resource.getrlimit(resource.RLIMIT_NOFILE)[1]
    if (nofile == resource.RLIM_INFINITY):
        nofile = maxfd # don't try to close infinite file descriptors
    for fd in range(0, nofile):
        try:
            os.close(fd)
        except OSError:	# fd wasn't open to begin with
            pass

    os.open(redirect_to, os.O_RDWR)	    # standard input (0)
    os.dup2(0, 1)			            # standard output (1)
    os.dup2(0, 2)			            # standard error (2)

    return(0)
