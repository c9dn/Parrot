#copyright Parrot,ParrotDevs,and ParrotMascot
#Last updated: 5/25/21
#Authors:Fruity Animations
#Please respect parrot's right's to this converter
import time
import os
import sys
import functions.header as header
import functions.image as image
import functions.syscmds as syscmds


try:
  upload = sys.argv[2]
except:
  quit(print("Excepted 1 argument 'upload html file',recived none"))

try:
  path = sys.argv[1]
except:
  quit(print("Excepted 1 argument 'md file',recived none"))

if os.path.exists(sys.argv[1]):
  pass
else:
  quit(print("Path not exists"))
file = open(sys.argv[1],"r")
Lines = file.readlines()
  
for line in Lines:

  #all of the possible headers in the markdown syntax
  if line.startswith("# "):
    header.header(line,"h1",upload)
  elif line.startswith("## "):
    header.header(line,"h2",upload)
  elif line.startswith("### "):
    header.header(line,"h3",upload)
  elif line.startswith("#### "):
    header.header(line,"h4",upload)
  elif line.startswith("##### "):
    header.header(line,"h5",upload)
  elif line.startswith("// "):
    syscmds.syscmds(line,upload)
  elif line.startswith("![]"):
    image.image(line,upload)
  elif line.startswith(" "):
    pass
  elif line.startswith(""):
    pass
  else:
    quit(print("Issue: We don't have support for the command:" +line+ " Sorry about this invonviniance,you can always recommend commands though"))

file = open("index.html","a")
file.write('\n<!-- Do No Delete Below,Under Law --> \n<footer style="font-family:Arial;">This static webpage was made using parrot.</footer>')
file.close()

quit(print("Finished Process,Leaving Program"))
#copyright Parrot,ParrotDevs,and ParrotMascot



