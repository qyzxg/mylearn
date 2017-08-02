#!/usr/bin/python
# -*- coding:utf-8 -*-

import random
from string import ascii_letters, digits

from werkzeug.security import generate_password_hash


def rcode(m=5, n=5, s='-'):
    """
    in:rcode(5, 4, '-')
    out:9VkQ-qgpX-KACL-dR9I-75qK
    :param m: 表示段数
    :param n: 表示每段字符数
    :param s: 表示连接符
    :return:返回生成的注册码
    """
    all_list = ascii_letters + digits

    code = str(('{}' + s) * int(m)).format(*[''.join \
                                                 (random.sample(all_list, int(n))) for i in range(m)])

    return generate_password_hash(code[:-1])


if __name__ == '__main__':
    for i in range(10):
        print(str(i + 1), rcode(5, 20, '|'))
