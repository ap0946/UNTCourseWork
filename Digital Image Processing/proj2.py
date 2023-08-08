from PIL import Image, ImageFilter

def totalEnergy(img, w, h):
    sum = 0
    for i in range(0, w):
        for j in range(0, h):
            pix_val = img.getpixel((i, j))
            sum += pix_val
    return sum

#lists to store the data values
X = []
Y = []

#open the images
img1 = Image.open('noisy-elliptical-object.png')
img2 = Image.open('noisy-elliptical-object.png')

pix1 = img1.load()
pix2 = img2.load()
w1, h1 = img1.size
w2, h2 = img2.size

#Image 1: Gaussian Filter
energy = totalEnergy(img1, w1, h1)
X.append(energy)
count = 0
filter_temp = img1
for i in range(0, 1000):
    filter_temp = img1.filter(ImageFilter.Kernel((3, 3), (1/16, 2/16, 1/16, 2/16, 4/16, 2/16, 1/16, 2/16, 1/16), 1, 0))
    img1 = filter_temp
    count += 1
    if count == 100:
        energy = totalEnergy(img1, w1, h1)
        X.append(energy)
        count = 0

#Image 2: Averaging Filter
energy = totalEnergy(img2, w2, h2)
Y.append(energy)
count = 0
filter_temp = img2
for i in range(0, 1000):
    filter_temp = img2.filter(ImageFilter.Kernel((3, 3), (1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9, 1/9), 1, 0))
    img2 = filter_temp
    count += 1
    if count == 100:
        energy = totalEnergy(img2, w2, h2)
        Y.append(energy)
        count = 0

print (X)
print (Y)

img1.save('filtered_img1.png')
img2.save('filtered_img2.png')

del X
del Y
