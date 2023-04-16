
#
#1. The user is redirected to the login page if he/she is not logged in.
#2. The user is redirected to the user page if he/she is logged in.
#3. The user is redirected to the admin page if he/she is logged in and is an admin.
#



#!/usr/bin/env python

import sys
import os
import time
import getopt
import socket
import ConfigParser
import struct
import binascii

# telnetlib.py
# Copyright (C) 2005-2006 Michael Foord
# E-mail: fuzzyman AT voidspace DOT org DOT uk

# telnetlib.py - Telnet client class.

# This software is licensed under the terms of the BSD license.
# http://www.voidspace.org.uk/python/license.shtml

# Telnet Commands

SE = 240
NOP = 241
DM = 242
BRK = 243
IP = 244
AO = 245
AYT = 246
EC = 247
EL = 248
GA = 249
SB = 250
WILL = 251
WONT = 252
DO = 253
DONT = 254
IAC = 255

# The following are not Telnet commands, but are used in this module.

BINARY = chr(0)
ECHO = chr(1)
RCP = chr(2)
SGA = chr(3)
NAMS = chr(4)
STATUS = chr(5)
TM = chr(6)
RCTE = chr(7)
NAOL = chr(8)
NAOP = chr(9)
NAOCRD = chr(10)
NAOHTS = chr(11)
NAOHTD = chr(12)
NAOFFD = chr(13)
NAOVTS = chr(14)
NAOVTD = chr(15)
NAOLFD = chr(16)
XASCII = chr(17)