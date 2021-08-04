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
        inimg.putpixel((ct, line), (r, g, b))
        ct += 1
        g +=1
        print('4')

    line += 1
    ct = 1
    g = 0

    while b != max:
        inimg.putpixel((ct, line), (r, g, b))
        ct += 1
        b +=1
        print('5')

    line += 1
    ct = 1
    b = 0

    while r != max:
        inimg.putpixel((ct, line), (r, g, b))
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
        print('7')

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
    ''' These colors might not be needed. set height to 11 else 6
    while r != max:
        inimg.putpixel((ct, line), (r, 255, b))
        ct += 1
        r += 1
        #b += 1
        print('9')

    line += 1
    ct = 1
    b = 0
    r = 0

    while g != max:
        inimg.putpixel((ct, line), (255, g, b))
        ct += 1
        g += 1
        #b += 1
        print('10')

    line += 1
    ct = 1
    b = 0
    g = 0

    while r != max:
        inimg.putpixel((ct, line), (r, g, 255))
        ct += 1
        r += 1
       # g += 1
        print('11')

    line += 1
    ct = 1
    b = 0
    g = 0
    '''
    inimg.save('init.jpg')
    inimg.close
    img = Image.open('init.jpg').convert('LA')
    img.save('initbw.png')
    img.close()
    img = Image.open('initbw.png').convert('RGB')
    img.save('initbw.jpg')
    img.close


def database_init():
    im2 = Image.open('init.jpg')
    im1 = Image.open('initbw.jpg')
    width = 255
    height = 5
    ic = 0
    hc = 0
    print('Creating Database file')
    g = open('data.txt', 'w+')
    print('Loading Images...')
    print('populating database file...')
    while hc != height:
        print('.')
        print(str(ic))
        print(str(hc))
        while ic != width:
            coordinate = ic, hc
            print(str(coordinate))
            g.write(str(im1.getpixel(coordinate)) + ' : ' + str(im2.getpixel(coordinate)) + '\n')
            ic += 1
        #readertwo(hc)
        hc +=1
        ic = 0
        print(str(hc))
        print('...')

    g.close

    print('Database Finished.')

def readertwo(r_height):
    ic = 1
    width = 256
    while ic != width:
        g.write(str(pix1.getpixel(c, r_height)))
        ic += 1

def picproc():
    global pix
    global f
    global width, height
    im = Image.open('test.jpg')
    # Get width and height as int
    width, height = im.size
    print(width, height)
    print(im.format, im.mode)
    pix = im.load
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
        f.write(str(pix[ic, r_height]))
        ic += 1

if os.path.exists('uni.colour') != True:
    print('DB doest not exist. Please initialize.')
    init()








#init()
database_init()
#picproc()

print('all done')
