#copyright Parrot,ParrotDevs,and ParrotMascot
#Last updated: 5/25/21
#Authors:Fruity Animations
#Please respect parrot's right's to this converter
def header(line,headertype,file):

  extras = ""
  outer = ""
  outer1 = ""
  try:cmd = line.split("!",1)[1]
  except: cmd = line



  #handeling extras
  if "font" in cmd:
    font = line.split("font",1)[1]
    font = font[1:]
    extras = extras + f'style="font-family:{font};"'
  if "color" in cmd:



    
    color = line.split("color",1)[1]
    color = color[1:]
    if "style" in extras:
      global temp
      temp = extras[:-1]
      temp = temp[:-len(color)]
      temp = temp[:-9]
      temp = temp + ";"
      temp = temp + f"color:{color};"
      temp = temp + '"'
      extras = temp
  if "center" in cmd:
    outer = outer + "<center>"
    
    outer1 = outer1 + "</center>"
    extras = extras[:-11]
    extras = extras + ';"'

    #extras = extras + f' style="color:{color}"'
  thing = ""

  
  pstcmd = len(cmd) + 1
  
  line = line[:-pstcmd]
  line = line[1:]
  if headertype == "h2":
    line = line[1:]
  elif headertype == "h3":
    line = line[2:]
  elif headertype == "h4":
    line = line[3:]
  elif headertype == "h5":
    line = line[4:]
  file = open(file,"a")
  file.write(f"{outer}<{headertype} {extras}>{line}</{headertype}>{outer1}\n")
  file.close()
