#!/usr/bin/python
# -*- coding:utf-8 -*-

from pyecharts import Bar

bar = Bar("我的第一个图表", "这里是副标题")
bar.add("服装", ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"], [5, 20, 36, 10, 75, 90])
bar.show_config()
# bar.render()

attr = ["衬衫", "羊毛衫", "雪纺衫", "裤子", "高跟鞋", "袜子"]
v1 = [5, 20, 36, 10, 75, 90]
v2 = [10, 25, 8, 60, 20, 80]
bar2 = Bar("柱状图数据堆叠示例")
bar2.add("商家A", attr, v1, is_stack=True)
bar2.add("商家B", attr, v2, is_stack=True)
bar2.render()