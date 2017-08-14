#!/usr/bin/env python3
import argparse, os, sys, re
from random import randint as ri
from subprocess import run
from shlex import quote
from shutil import copy
from math import ceil

### Setup argument parser
parser = argparse.ArgumentParser(description='Backup scoreboards to GitHub.')
parser.add_argument('-u','--url',default='http://localhost:8080/',
                    help='Source URL')
parser.add_argument('-p','--period',type=float,default=30.0,
                    help='Push period in seconds (default: %(default)s)')
parser.add_argument('-d','--destination',default='')

### Parsing the arguments
res = parser.parse_args()

