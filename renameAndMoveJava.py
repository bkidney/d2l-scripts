import os
import sys

path = ""

if (len(sys.argv) > 1):
    path = sys.argv[1]
if (path == ""):
    path = os.getcwd()

print("Working in: " + path)

files = os.listdir(path)
moves = [] 
for f in files:
    parts = f.split('- ')
    moves.append({parts[1]: parts[3].lstrip()})

    dir = "".join( parts[1].split() )
    jfile = "".join( parts[3].split() )

    print(f + "->" + dir + "/" + jfile)
    if (not os.path.exists(dir)):
        os.mkdir(dir)

    os.rename(f, dir + "/" + jfile)