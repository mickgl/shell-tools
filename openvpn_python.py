#!/usr/bin/env python3
# Tool to automatizate connections to OpenVPN from command line

import os
import subprocess
import argparse
import sys
import random

c = argparse.ArgumentParser(prog="openvpn_python", description="Connect to openvpn")
c.add_argument("-c", help="Specify country", required=True)
args = c.parse_args()

fname = ".ovpn" # Add rest of the path

def file():
    global path
    nmr = random.randrange(1020)
    country = sys.argv[2]
    path = country + str(nmr) + fname

if args.c:
    file()
    while os.path.exists(path) != True:
        file()
    subprocess.run(["sudo", "openvpn", path])
else:
    print("Error")
