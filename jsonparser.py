#!/usr/bin/python
# -*- coding:utf-8 -*-

# encoding: utf-8
'''
Author:Siukwan
'''


# reload(sys)
# sys.setdefaultencoding('utf8')
# import json


def txt2str(file='jsondata2.txt'):
    '''
    打开指定的json文件
    '''
    fp = open(file)
    allLines = fp.readlines()
    fp.close()
    str = ""
    for eachLine in allLines:
        # eachLine=ConvertCN(eachLine)

        # 转换成字符串
        for i in range(0, len(eachLine)):
            # if eachLine[i]!= ' ' and eachLine[i]!= '	' and eachLine[i]!='\n': #删除空格和换行符，但是json双引号中的内容空格不能删除
            str += eachLine[i]
    return str


class jsonparser:
    def __init__(self, str=None):
        self._str = str
        self._index = 0

    def _skipBlank(self):
        '''
        跳过空白、换行或tab： \n\t\r
        '''
        while self._index < len(self._str) and self._str[self._index] in ' \n\t\r':
            self._index = self._index + 1

    def parse(self):
        '''
        进行解析的主要函数
        '''
        self._skipBlank()
        if self._str[self._index] == '{':
            self._index += 1
            return self._parse_object()
        elif self._str[self._index] == '[':
            self._index += 1
            return self._parse_array()
        else:
            print
            "Json format error!"

    def _parse_string(self):
        '''
        找出两个双引号中的string
        '''
        begin = end = self._index
        # 找到string的范围
        while self._str[end] != '"':
            if self._str[end] == '\\':  # 重点！出现\，表明其后面的是配合\的转义符号，如\",\t,\r，主要针对\"的情况
                end += 1
                if self._str[end] not in '"\\/bfnrtu':
                    print
            end += 1
        self._index = end + 1
        return self._str[begin:end]

    def _parse_number(self):
        '''
        数值没有双引号
        '''
        begin = end = self._index
        end_str = ' \n\t\r,}]'  # 数字结束的字符串
        while self._str[end] not in end_str:
            end += 1
        number = self._str[begin:end]

        # 进行转换
        if '.' in number or 'e' in number or 'E' in number:
            res = float(number)
        else:
            res = int(number)
        self._index = end
        return res

    def _parse_value(self):
        '''
        解析值，包括string，数字
        '''
        c = self._str[self._index]

        # 解析对象
        if c == '{':
            self._index += 1
            self._skipBlank()
            return self._parse_object()
        # 解析数组
        elif c == '[':
            # array
            self._index += 1
            self._skipBlank()
            return self._parse_array()
        # 解析string
        elif c == '"':
            # string
            self._index += 1
            self._skipBlank()
            return self._parse_string()
        # 解析null
        elif c == 'n' and self._str[self._index:self._index + 4] == 'null':
            # null
            self._index += 4
            return None
        # 解析bool变量true
        elif c == 't' and self._str[self._index:self._index + 4] == 'true':
            # true
            self._index += 4
            return True
        # 解析bool变量false
        elif c == 'f' and self._str[self._index:self._index + 5] == 'false':
            # false
            self._index += 5
            return False
        # 剩下的情况为number
        else:
            return self._parse_number()

    def _parse_array(self):
        '''
        解析数组
        '''
        arr = []
        self._skipBlank()
        # 空数组
        if self._str[self._index] == ']':
            self._index += 1
            return arr
        while True:
            val = self._parse_value()  # 获取数组中的值，可能是string，obj等等
            arr.append(val)  # 添加到数组中
            self._skipBlank()  # 跳过空白
            if self._str[self._index] == ',':
                self._index += 1
                self._skipBlank()
            elif self._str[self._index] == ']':
                self._index += 1
                return arr
            else:
                print
                "array parse error!"
                return None

    def _parse_object(self):
        '''
        解析对象
        '''
        obj = {}
        self._skipBlank()
        # 空object
        if self._str[self._index] == '}':
            self._index += 1
            return obj
        # elif self._str[self._index] !='"':
        # 报错

        self._index += 1  # 跳过当前的双引号
        while True:
            key = self._parse_string()  # 获取key值
            self._skipBlank()

            self._index = self._index + 1  # 跳过冒号:
            self._skipBlank()

            # self._index = self._index+1#跳过双引号
            # self._skipBlank()
            # 获取value值,目前假设只有string的value和数字
            obj[key] = self._parse_value()
            self._skipBlank()
            # print key,":",obj[key]
            # 对象结束了，break
            if self._str[self._index] == '}':
                self._index += 1
                break
            elif self._str[self._index] == ',':  # 还存在其他对象
                self._index += 1
                self._skipBlank()

            self._index += 1  # 跳过下一个对象的第一个双引号

        return obj  # 返回对象

    def display(self):
        displayStr = ""
        self._skipBlank()
        while self._index < len(self._str):
            displayStr = displayStr + self._str[self._index]
            self._index = self._index + 1
            self._skipBlank()
        print
        displayStr


def _to_str(pv):
    '''把python变量转换成string'''
    _str = ''
    if type(pv) == type({}):
        # 处理对象
        _str += '{'
        _noNull = False
        for key in pv.keys():
            if type(key) == type(''):
                _noNull = True  # 对象非空
                _str += '"' + key + '":' + _to_str(pv[key]) + ','
        if _noNull:
            _str = _str[:-1]  # 把最后的逗号去掉
        _str += '}'

    elif type(pv) == type([]):
        # 处理数组
        _str += '['
        if len(pv) > 0:  # 数组不为空,方便后续格式合并
            _str += _to_str(pv[0])
        for i in range(1, len(pv)):
            _str += ',' + _to_str(pv[i])  # 因为已经合并了第一个，所以可以加逗号
        _str += ']'

    elif type(pv) == type(''):
        # 字符串
        _str = '"' + pv + '"'
    elif pv == True:
        _str += 'true'
    elif pv == False:
        _str += 'false'
    elif pv == None:
        _str += 'null'
    else:
        _str = str(pv)
    return _str


# main函数
if __name__ == '__main__':
    "test"
    '''
    jsonInstance=jsonparser(txt2str())
    jsonTmp = jsonInstance.parse()
    print jsonTmp
    print jsonTmp['obj1']['family']['father']
    print jsonTmp['obj1']['family']['sister']
    print ' '
    jsonInstance=jsonparser(txt2str('jsondataArray.txt'))
    jsonTmp = jsonInstance.parse()
    print jsonTmp
    print ' '
    '''
    jsonInstance = jsonparser(txt2str('jsonTestFile.txt'))
    jsonTmp = jsonInstance.parse()
    print(jsonTmp)
    print(_to_str(jsonTmp))

    jsonInstance = jsonparser(txt2str('json.txt'))
    jsonTmp = jsonInstance.parse()
    print(jsonTmp)

    print(_to_str(jsonTmp))
