try:
  from PIL import Image, ImageFilter
except ImportError as e:
  print(e)
try:
  from random import randint,randint,shuffle,seed
except ImportError as e:
  print(e)



def effect(path,path_save):
  
  mas = []
  n = 0
  try:
    img = Image.open(path)
  except Exception as e:
    print(e)
  size = img.size

  for x in range(0,size[0]):
    for y in range(0,size[1]):
      color = img.getpixel((x,y)) 
      mas.append(color)
  for m in range(0,len(mas)):
     k = randint(0,2)
     if k == 1:
       mas[m] = mas[m-1]
     else:
       pass
  for x in range(0,size[0]):
    for y in range(0,size[1]):
       img.putpixel((x,y),mas[n])
       n += 1
  img.save(path_save,img.format)

