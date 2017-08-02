#!/usr/bin/python
# -*- coding:utf-8 -*-

import os

from PIL import Image


def cver_rep(img_dir, width=640, height=1136):
    images = []
    for filename in os.listdir(img_dir):
        images.append(os.path.join(os.path.abspath(img_dir), filename))
    for img in images:
        im = Image.open(img)
        w, h = im.size
        if w > width:
            w, h = width, int(h * width / w)
        elif h > height:
            h, w = height, int(w * height / h)
        im_new = im.resize((w, h), resample=Image.LANCZOS)
        im_new.save(os.path.join(os.path.abspath(img_dir),
                                 '{}x{}-'.format(h, w) + os.path.basename(im.filename)))


cver_rep('./images')
