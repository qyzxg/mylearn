#!/usr/bin/python
# -*- coding:utf-8 -*-

def code_count(code_path):
    code = 0  # 代码行数
    comment = 0  # 注释行数
    b = 0  # 空行行数
    with open(code_path, 'r', encoding='utf-8') as file:
        for line in file.readlines():
            if not line.strip():
                b += 1
            elif line.strip().startswith('#'):
                comment += 1
            else:
                code += 1

    return code, comment, b


if __name__ == '__main__':
    x, y, z = code_count('./text/code.txt')
    print('代码:{}行,注释:{}行,空行:{}行,共:{}行'.format(x, y, z, x + y + z))
