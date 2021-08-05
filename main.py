from PIL import Image
import os
import re
import time

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
    print('Creating data image set.')
    while r != max:
        inimg.putpixel((ct, line), (r, g, b))
        ct += 1
        r +=1

    line += 1
    r = 0
    ct = 1

    while g != max:
        inimg.putpixel((ct, line), (r, g, b))
        ct += 1
        g +=1

    line += 1
    ct = 1
    g = 0

    while b != max:
        inimg.putpixel((ct, line), (r, g, b))
        ct += 1
        b +=1

    line += 1
    ct = 1
    b = 0

    while r != max:
        inimg.putpixel((ct, line), (r, g, b))
        ct += 1
        r +=1
        g += 1

    line += 1
    ct = 1
    g = 0
    r = 0

    while g != max:
        inimg.putpixel((ct, line), (r, g, b))
        ct += 1
        g += 1
        b += 1

    line += 1
    ct = 1
    g = 0
    b = 0

    while r != max:
        inimg.putpixel((ct, line), (r, g, b))
        ct += 1
        r += 1
        b += 1

    line += 1
    ct = 1
    b = 0
    r = 0

    inimg.save('init.jpg')
    inimg.close
    img = Image.open('init.jpg').convert('LA')
    img.save('initbw.png')
    img.close()
    print('Converting to black and white.')
    img = Image.open('initbw.png').convert('RGB')
    img.save('initbw.jpg')
    img.close
    print('Images created.')
    database_init()


def database_init():
    im2 = Image.open('init.jpg')
    im1 = Image.open('initbw.jpg')
    width = 255
    height = 5
    ic = 0
    hc = 0
    bwread = 0, 0, 0
    bwreadold = 0, 0, 0
    print('Creating Database file')
    g = open('data.txt', 'w+')
    print('Loading Images...')
    print('populating database file...')
    while hc != height:
        while ic != width:
            coordinate = ic, hc
            bwread = im1.getpixel(coordinate)
            if bwread != bwreadold:
                g.write(str(im1.getpixel(coordinate)) + ' : ' + str(im2.getpixel(coordinate)) + '\n')
            bwreadold = im1.getpixel(coordinate)
            ic += 1
        hc +=1
        ic = 0

    g.close
    print('Database Finished.')

def picproc(file):
    tic = time.perf_counter()
    im = Image.open(file)
    height, width = im.size
    im2 = Image.new(mode="RGB", size=(height, width))
    print(width, height)
    print(im.format, im.mode)
    maxpix = height * width
    matchcount = 0
    pixcount = 0
    old = (0, 0, 0)
    for x in range(height):
        for y in range(width):
            coordinate = x, y
#            print(str(coordinate))
            bw1 = im.getpixel(coordinate)
            if bw1 != old:
                if bw1 != (255, 255, 255) or (0, 0, 0):
                    with open('data.txt', 'r') as g:
                        lines = g.readlines()
                        for line in lines:
                            if re.search(str(bw1), line):
                                bw, rgb = line.split(' : ')
                                rgb = rgb.replace('(', '')
                                rgb = rgb.replace(')', '')
                                rgbt = tuple(map(int, rgb.split(', ')))
                                matchcount +=1
                                print('Found match')
                            else:
                                rgbt = bw1

                elif bw1 == (255, 255, 255):
                    rgbt = 255, 255, 255

                elif bw1 == (0, 0, 0):
                    rgbt = (0, 0, 0)

                else:
                    print('Something is going wrong.')
            else:
                print('Duplicate detected. Using Old Value.')
            im2.putpixel(coordinate, rgbt)
            old = im.getpixel(coordinate)
            pixcount += 1
            done = pixcount / maxpix
            prog = round(done * 100, 2)
            print('Progress : ' + str(prog) + '%')
    savef, extf = filename.split('.')
    im2.save(savef + '.jpg')
    im2.close()
    toc = time.perf_counter()
    print('Found ' + str(matchcount) + ' out of ' + str(maxpix) + ' pixel matches...')
    print(f' in {toc - tic:0.4f} seconds')

if os.path.exists('data.txt') != True:
    print('DB doest not exist. Creating files... Please wait.')
    init()

print('Enter File name : ')
filename = input()

picproc(filename)

