try:
  from PIL import Image, ImageFilter
except ImportError as e:
  print(e)
try:
  from random import randint,randint,shuffle,seed
except ImportError as e:
  print(e)
try:
  from sys import exit,argv
except ImportError as e:
  print(e)

def effect():
  mas = []
  n = 0
  path = argv[1]
  img = Image.open(path)
  size = img.size

  for x in range(0,size[0]):
    for y in range(0,size[1]):
      color = img.getpixel((x,y)) 
      mas.append(color)
  for m in range(0,len(mas)):
     k = randint(0,3)
     if k == 1:
       mas[m] = mas[m-1]
     else:
       pass
  for x in range(0,size[0]):
    for y in range(0,size[1]):
       img.putpixel((x,y),mas[n])
       n += 1
  img.show()
      
def effect_2():

  masr = []
  masg = []
  masb = []

  for x in range(0,size[0]):
    for y in range(0,size[1]):
      r,g,b = img.getpixel((x,y)) 
      masr.append(r)
      masg.append(g)
      masb.append(b)
  masb.sort(reverse=True)
  masr.sort()

  n = 0

  for x in range(0,size[0]):
    for y in range(0,size[1]):
      img.putpixel((x,y),(masr[n],masg[n],masb[n]))
      n += 1
  img.show()
