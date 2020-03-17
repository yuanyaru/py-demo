#!/usr/bin/python

import os
import sys


if len(sys.argv) < 3:
    print "please input two arguments"
    sys.exit(1)

arg0 = sys.argv[1]
arg1 = sys.argv[2]

os.system('hello.sh '+arg0+' '+arg1)
