from PIL import Image
import os

wig = (255, 255, 255)
bigg = (0, 0, 0)

def init():
    r = 0
    g = 0
    b = 0
    max = 254
    #y
    ct = 1
    #X
    line = 0

    inimg = Image.new('RGB', (255, 6))
    print('1')
    while r != max:
        print('2')
        inimg.putpixel((ct, line), (r, g, b))
        ct += 1
        print(str(ct))
        r +=1

    line += 1
    r = 0
    ct = 1

    while g != max:
        inimg.putpixel((ct,line),(r, g, b))
        ct += 1
        g +=1
        print('4')

    line += 1
    ct = 1
    g = 0

    while b != max:
        inimg.putpixel((ct,line),(r, g, b))
        ct += 1
        b +=1
        print('5')

    line += 1
    ct = 1
    b = 0

    while r != max:
        inimg.putpixel((ct,line),(r, g, b))
        ct += 1
        r +=1
        g += 1
        print('6')

    line += 1
    ct = 1
    g = 0
    r = 0

    while g != max:
        inimg.putpixel((ct, line), (r, g, b))
        ct += 1
        g += 1
        b += 1
        print('6')

    line += 1
    ct = 1
    g = 0
    b = 0

    while r != max:
        inimg.putpixel((ct, line), (r, g, b))
        ct += 1
        r += 1
        b += 1
        print('6')

    line += 1
    ct = 1
    b = 0
    r = 0

    inimg.save('init.jpg')
    inimg.show()







def picproc():
    global pix
    global f
    global width, height
    im = Image.open('test.jpg')
    # Get width and height as int
    width, height = im.size
    print(width, height)
    print(im.format, im.mode)
    pix = im.load()
    f = open('test.txt', 'w+')
    ct = 1
    while ct != height:
        readerro(ct)
        f.write(str(ct) and '\n')
        ct += 1

    f.close()


def readerro(r_height):
    ic = 1
    while ic != width:
        if pix[ic, r_height] != wig and pix[ic, r_height] != bigg:
            f.write(str(pix[ic, r_height]))
        ic += 1

if os.path.exists('uni.colour') != True:
    print('DB doest not exist. Please initialize.')
    init()








init()
picproc()

print('all done')
