#!/usr/bin/python
# -*- coding:utf-8 -*-

import jieba
import matplotlib.pyplot as plt
import numpy as np
from PIL import Image
from wordcloud import WordCloud


def word_img(img, text):
    font = './fonts/STLITI.TTf'
    alice_mask = np.array(Image.open(img))
    wordcloud = WordCloud(font_path=font, background_color='white',
                          margin=5, mask=alice_mask,mode="RGB",
                          max_words=200, max_font_size=120, random_state=2)
    word_list = []
    with open(text, 'r', encoding='utf-8', errors='ignore') as f:
        words = list(jieba.cut(f.read()))
        for word in words:
            if len(word) > 2:
                word_list.append(word)
    txt = ' '.join(word_list)
    wordcloud = wordcloud.generate(txt)
    wordcloud.to_file('./images/word_cloud_description.jpg')
    plt.imshow(wordcloud)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    word_img('./images/boy.jpg', './text/description.txt')
