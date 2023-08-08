#NAME: Alexis Phu

from PIL import Image
import math

#read the original image
img = Image.open('noisy-elliptical-object.png')
pix_arr = img.load()
width, height = img.size

#use the size of the image to determine processing range
mid_x = width/2
mid_y = height/2
r = pow(50, 2)

w1 = int(mid_x - 50)
w2 = int(mid_x + 50)
h1 = int(mid_y - 50)
h2 = int(mid_y + 50)

#modify pixels within circle
for i in range(w1, w2):
        for j in range(h1, h2):
            if ((pow((i-mid_x), 2) + pow((j-mid_y), 2)) <= r):
                pix_arr[i, j] = 0;

#save the new image
img.save('new_image.png')

#print the image
new_img = Image.open('new_image.png')
new_img.show()
