from distutils.core import setup
import py2exe
import sys
# sys.setrecursionlimit(4000)
setup(console=['req.py'])
#python setup.py py2exe