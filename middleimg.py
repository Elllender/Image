from PIL import Image
from math import floor
from random import shuffle

img2 = Image.open('1.jpg')
img1 = Image.open('2.jpg')

size = img1.size
f = img1.format
mode = img1.mode

mas1 = []
mas2 = []

new_img = Image.new(mode, (size[0], size[1]), (255, 255, 255))

for x in range(0, size[0]):
    for y in range(0, size[1]):
        r, g, b = img1.getpixel((x, y))
        mas1.append((r, g, b, (x, y)))
        r2, g2, b2 = img2.getpixel((x, y))
        mas2.append((r2, g2, b2, (x, y)))

mas1.sort(key=lambda x: x[1])
mas2.sort(key=lambda x: x[1])
# shuffle(mas1)
# shuffle(mas2)
n = 0

mas_new = []

for i in range(0, len(mas1)):
        r = mas1[i][0] + mas2[i][0]  # 1 + 1
        d = floor(r / 2)
        r2 = mas1[i][1] + mas2[i][1]
        d2 = floor(r2 / 2)
        r3 = mas1[i][2] + mas2[i][2]
        d3 = floor(r3 / 2)
        mas_new.append((d, d2, d3, (mas2[i][3][0], mas2[i][3][1])))

for k in range(0, len(mas_new)):
    new_img.putpixel((mas_new[k][3][0], mas_new[k][3][1]), (mas_new[k][0], mas_new[k][1], mas_new[k][2]))

new_img.show()
'''for x in range(0, new_img.size[0]):
    for y in range(0, new_img.size[1]):
        c = new_img.getpixel((x, y))
        if c == ():
            new_img.putpixel((x, y), (15, 22, 33))
        else:
            pass'''
