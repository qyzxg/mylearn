#!/usr/bin/python
# -*- coding:utf-8 -*-
from textrank4zh import TextRank4Sentence

with open('t_post.txt', 'r', encoding='utf-8') as f:
    file = f.read()
    # print(file)
    tr4s = TextRank4Sentence()
    tr4s.analyze(text=file, lower=True, source='all_filters')
    for item in tr4s.get_key_sentences(num=3, sentence_min_len=8):
        print(item.index, item.weight, item.sentence)
