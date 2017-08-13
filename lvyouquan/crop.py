#!/usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image
import hashlib
import time
import math
import os

def crop(img):
    im = Image.open(img)
    im.convert("P")
    im2 = Image.new("P", im.size, 255)
    for x in range(im.size[1]):
        for y in range(im.size[0]):
            pix = im.getpixel((y, x))
            if pix == 86 or pix == 85 or pix == 45 or pix == 46 or pix == 44:  # these are the numbers to get
                im2.putpixel((y, x), 0)

    inletter = False
    foundletter = False
    start = 0
    end = 0

    letters = []

    for y in range(im2.size[0]):
        for x in range(im2.size[1]):
            pix = im2.getpixel((y, x))
            if pix != 255:
                inletter = True
        if foundletter == False and inletter == True:
            foundletter = True
            start = y

        if foundletter == True and inletter == False:
            foundletter = False
            end = y
            letters.append((start, end))

        inletter = False

    count = 0
    for letter in letters:
        m = hashlib.md5()
        im3 = im2.crop((letter[0], 0, letter[1], im2.size[1]))
        a = "{}{}".format(time.time(), count)
        b = a.encode('utf-8')
        m.update(b)
        im3.save("./%s.gif" % (m.hexdigest()))
        count += 1

# crop('1.gif')

p = os.path.join(os.getcwd(),'code')
for i in os.listdir(p):
    crop('./code/{}'.format(i))