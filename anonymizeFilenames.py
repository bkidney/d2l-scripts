import os
import sys

path = ""

if (len(sys.argv) > 1):
    path = sys.argv[1]
if (path == ""):
    path = os.getcwd()

files = os.listdir(path)
moves = [] 
for f in files:
    if f == "index.html":
      os.remove(f)
    else:
      parts = f.split('- ')
      if len(parts) > 1:

          parts[1] = ""
          anonymized = "".join( parts )
      
          os.rename(f, anonymized)
    
