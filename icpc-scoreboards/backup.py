#!/usr/bin/env python3
import argparse, os, sys, re, time
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
parser.add_argument('-r','--repeat',type=int,default=500,
                    help='Times to repeat (default: %(default)d)')
parser.add_argument('-d','--destination',default='.',
                    help='Destination path (default: %(default)s)')

### Parsing the arguments
res = parser.parse_args()
url = res.url
period = res.period
dest = res.destination
repeat = res.repeat

if dest != '.':
    os.mkdirs(dest,exist_ok=True)

for _ in range(repeat):
    run(['touch',dest+'/index.html'])
    run(['rm',dest+'/index.html'])
    run(['wget','-P',dest,url])
    run(['git','add','.'])
    run(['git','commit','-m','"update"'])
    run(['git','push'])
    time.sleep(period)
