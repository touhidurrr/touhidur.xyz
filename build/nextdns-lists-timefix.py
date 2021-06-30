#!/usr/bin/python3

from glob import glob
from datetime import datetime

filePaths = glob('filterlists/nextdns-*')

for path in filePaths:

  lines = []

  with open(path, mode = 'r', encoding = 'utf-8') as f:
    lines = f.readlines()

  lines[7] = '# Updated: ' + datetime.utcnow().strftime('%a, %d %b %y %H:%M:%S') + '\n'

  with open(path, mode = 'w', encoding = 'utf-8') as f:
    f.write(''.join(lines))
