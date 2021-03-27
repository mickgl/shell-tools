#!/usr/bin/python3

import urllib.request
import sys

def usage():
    print("Check if website contain pattern")
    print()

    print("Usage: check_site.py [pattern] [link to site]")
    print()
    sys.exit(0)

if not len(sys.argv[2:]):
    usage()

name = sys.argv[2]
string = sys.argv[1]

get = urllib.request.urlopen(name)
out = get.read()

outdec = out.decode()

if string in outdec:
    print("True")
else:
    print("False")

get.close()

