import os
import sys
import platform

extension = ""
if platform.system() == "Windows":
    extension = ".exe"

path = ""
if (len(sys.argv) > 1):
    path = sys.argv[1]

if (path == ""):
    path = os.getcwd()

for dir, subdir, files in os.walk(path):
    for sd in subdir:
        os.chdir(sd)
        print(sd)
        sourcesfiles = os.listdir()
        for f in sourcesfiles:
            if f.endswith(".cpp"):
                fBase = os.path.splitext(os.path.basename(f))[0]
                os.system('clang++ ' + f + " -o " + fBase + extension)
            elif f.endswith(".c"):
                fBase = os.path.splitext(os.path.basename(f))[0]
                os.system('clang ' + f + " -o " + fBase + extension)
            elif f.endswith(".java"):
                os.system('javac ' + f)
        os.chdir('..')
        
