#Name: Alexis Phu
from PIL import Image, ImageFilter
import matplotlib.pyplot as plt
import math

img = Image.open('building.bmp')
img = img.convert("L")
pix = img.load()
w, h = img.size

#Gaussian Smoothing
img = img.filter(ImageFilter.Kernel((3, 3), (1/16, 2/16, 1/16, 2/16, 4/16, 2/16, 1/16, 2/16, 1/16), 1, 0))

#Sobel
Sobel_H_1 = img.filter(ImageFilter.Kernel((3, 3), (1, 2, 1, 0, 0, 0, -1, -2, -1), 1, 0))
Sobel_H_2 = img.filter(ImageFilter.Kernel((3, 3), (-1, -2, -1, 0, 0, 0, 1, 2, 1), 1, 0))
Sobel_H = Image.new(mode= 'L', size= (w, h))
for i in range (0, w):
    for j in range (0, h):
        pixval_H1 = Sobel_H_1.getpixel((i, j))
        pixval_H2 = Sobel_H_2.getpixel((i, j))
        if (pixval_H1 > pixval_H2):
            Sobel_H.putpixel((i, j), pixval_H1)
        else:
            Sobel_H.putpixel((i, j), pixval_H2)

Sobel_V_1 = img.filter(ImageFilter.Kernel((3, 3), (-1, 0, 1, -2, 0, 2, -1, 0, 1), 1, 0))
Sobel_V_2 = img.filter(ImageFilter.Kernel((3, 3), (1, 0, -1, 2, 0, -2, 1, 0, -1), 1, 0))
Sobel_V = Image.new(mode= 'L', size= (w, h))
for i in range (0, w):
    for j in range (0, h):
        pixval_V1 = Sobel_V_1.getpixel((i, j))
        pixval_V2 = Sobel_V_2.getpixel((i, j))
        if (pixval_V1 > pixval_V2):
            Sobel_V.putpixel((i, j), pixval_V1)
        else:
            Sobel_V.putpixel((i, j), pixval_V2)

Sobel_H.save("Sobel_H.bmp")
Sobel_V.save("Sobel_V.bmp")
combo = Image.new(mode= 'L', size= (w, h))
for i in range (0, w):
    for j in range (0, h):
        pixval_H = Sobel_H.getpixel((i, j))
        pixval_V = Sobel_V.getpixel((i, j))
        if ((pixval_H > 80) or (pixval_V > 80)):
            combo.putpixel((i, j), 255)
combo.save("Sobel.bmp")

#LaPlacian
LaPlacian_1 = img.filter(ImageFilter.Kernel((3, 3), (-1, -1, -1, -1, 8, -1, -1, -1, -1), 1, 0))
LaPlacian_2 = img.filter(ImageFilter.Kernel((3, 3), (1, 1, 1, 1, -8, 1, 1, 1, 1), 1, 0))
LaPlacian = Image.new(mode= 'L', size= (w, h))
for i in range (0, w):
    for j in range (0, h):
        pixval_1 = LaPlacian_1.getpixel((i, j))
        pixval_2 = LaPlacian_2.getpixel((i, j))
        if (pixval_1 > pixval_2):
            LaPlacian.putpixel((i, j), pixval_1)
        else:
            LaPlacian.putpixel((i, j), pixval_2)

LaPlacian_filtered = Image.new(mode= 'L', size= (w, h))
for i in range (0, w):
    for j in range (0, h):
        pixval = LaPlacian.getpixel((i, j))
        if ((pixval > 40)):
            LaPlacian_filtered.putpixel((i, j), 255)
LaPlacian_filtered.save("LaPlacian.bmp")

#Computations for comparison!
TP = 0
FP2 = 0
FP1 = 0
for i in range (0, w):
    for j in range(0, h):
        pixval_S = combo.getpixel ((i, j))
        pixval_L = LaPlacian_filtered.getpixel((i, j))
        if ((pixval_S > 0) and (pixval_L > 0)):
            TP += 1
        if ((pixval_L == 0) and (pixval_S > 0)):
            FP2 += 1
        if ((pixval_S == 0) and (pixval_L > 0)):
            FP1 += 1
P2 = TP/(TP + FP2)
P1 = TP/(TP + FP1)

print("TP= ", TP)
print ("FP1= ", FP1)
print ("FP2= ", FP2)
print ("P1= ", P1, "\nP2= ", P2)

fig, ax = plt.subplots()
ax.set_axis_off()
table = ax.table(
        cellText = [[TP, TP], [FP1, FP2], [P1, P2]],
        rowLabels = ('TP', 'FP', 'PRECISION'),
        colLabels = ('1', '2'),
        cellLoc = 'center',
        loc = 'upper center')
fig.savefig('Table.png')
