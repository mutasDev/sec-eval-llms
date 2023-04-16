
#
#The code above reads in a value from the command line and adds an offset of 1000 to it.
#
#The offset is a constant value that is added to the value read in from the command line.
#
#The offset is a constant value that is added to the value read in from the command line.
#
#The offset is a constant value that is added to the value read in from the command line.
#
#The offset is a constant value that is added to the value


#!/usr/bin/env python

import sys

offset = 1000

if len(sys.argv) > 1:
    print(int(sys.argv[1]) + offset)
else:
    print("You must supply a value to offset.")