from distutils.core import setup
import py2exe
import sys
sys.setrecursionlimit(4000)
setup(console=['playground.py'])
#python setup.py py2exe