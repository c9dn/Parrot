#copyright Parrot,ParrotDevs,and ParrotMascot
#Last updated: 5/25/21
#Authors:Fruity Animations
#Please respect parrot's right's to this converter

def syscmds(line,file):
  cmd = line.split("!",1)[1]
  if "backround" in cmd:
    backround = line.split("backround",1)[1]
    file = open(file,"a")
    file.write(f'<body style="background:{backround}"></body>\n')
    file.close()

  if "title" in cmd:
    title = line.split("title",1)[1]

    file = open(file,"a")
    file.write(f'<title>{title}</title>')
    file.close()