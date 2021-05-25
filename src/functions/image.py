#copyright Parrot,ParrotDevs,and ParrotMascot
#Last updated: 5/25/21
#Authors:Fruity Animations
#Please respect parrot's right's to this converter
def image(line,file):

  image = line[4:-1]
  file = open("index.html","a")
  file.write(f'<img src="{image}">')
  file.close()
