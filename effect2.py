try:
  from PIL import Image, ImageFilter
except ImportError as e:
  print(e)
try:
  from random import randint,randint,shuffle,seed
except ImportError as e:
  print(e)


def effect2(path,path_save):
  try:
    img = Image.open(path)
  except Exception as e:
    print(e)
    exit(1)
  size = img.size
  masr = []
  masg = []
  masb = []
  for x in range(0,size[0]):
    for y in range(0,size[1]):
      r,g,b = img.getpixel((x,y)) 
      masr.append(r)
      masg.append(g)
      masb.append(b)
  masb.sort()
  masb.sort(reverse=True)

  n = 0

  for x in range(0,size[0]):
    for y in range(0,size[1]):
      img.putpixel((x,y),(masr[n],masg[n],masb[n]))
      n += 1
  img.save(path_save,img.format)

