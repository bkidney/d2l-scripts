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
        print(sd)
        jfiles = os.listdir()
        for f in jfiles:
            fBase = os.path.splitext(os.path.basename(f))[0]
            os.system('clang++ ' + f + " -o " + fBase + ".exe")
        os.chdir('..')
