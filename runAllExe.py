

import os
import sys

path = ""
if (len(sys.argv) > 1):
    path = sys.argv[1]

if (path == ""):
    path = os.getcwd()

for dir, subdir, files in os.walk(path):
    for sd in subdir:
        os.chdir(sd)
        jfiles = os.listdir()
        for f in jfiles:
            if f.endswith('.exe'):
                print('---- ' + sd + '/' + f + ' ----')
                os.system(f)
                print("")
        os.chdir('..')
