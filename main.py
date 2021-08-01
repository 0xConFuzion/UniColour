from PIL import Image
wig = (255, 255, 255)
bigg = (0, 0, 0)
#Load image from file
im = Image.open('test.jpg')
#Get width and height as int
width, height = im.size
#Duhhhhh
print(width, height)
print(im.format, im.mode)
#load image into a readable state to call upon....
pix = im.load()
f = open('test.txt', 'w+')
def readerro(r_height):
    ic = 1
    while ic != width:
        if pix[ic, r_height] != wig and pix[ic, r_height] != bigg :
            f.write(str(pix[ic, r_height]))

        ic += 1
    ic = 1
ct = 1
while ct != height:
    readerro(ct)
    f.write(str(ct) and '\n')
    ct += 1

f.close()
print('all done')




