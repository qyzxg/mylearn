#!/usr/bin/python
# -*- coding:utf-8 -*-

from PIL import Image, ImageDraw, ImageFont


def img_text(img, s):
    if isinstance(img, Image.Image):
        im = img
    elif isinstance(img, str):
        im = Image.open(img)
    print(im.size)
    draw = ImageDraw.Draw(im)
    font = ImageFont.truetype(r"C:\\WINDOWS\\Fonts\\simkai.ttf", 24)

    draw.text((im.width - 100, 10), '%s' % s, font=font, fill=(255, 0, 0))
    im.save('img_text.jpg')
    im.show()


if __name__ == '__main__':
    img_text('n00004475_6590.jpg', '5')
