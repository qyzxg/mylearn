#!/usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image


def img_str(img, width, height):
    im = Image.open(img)
    im = im.resize((width, height), Image.ANTIALIAS)
    txt = ''
    for w in range(width):
        for h in range(height):
            txt += map_str(im.getpixel((w, h)))
        txt += '\n'
    return txt


def map_str(t):
    ascii_char = list(r"$@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~<>i!lI;:,\"^`'. ")
    length = len(ascii_char)
    gray = int(0.2126 * t[0] + 0.7152 * t[1] + 0.0722 * t[2])
    unit = (256.0 + 1) / length
    i = gray // unit
    return ascii_char[int(i)]

if __name__ == '__main__':
    print(img_str('boy.jpg', 30,40))
