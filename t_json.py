#!/usr/bin/python
# -*- coding:utf-8 -*-

import json

city = ['廊坊', '黄南藏族自治州', '平凉', '潮州', '抚州', '德阳', '昌吉回族自治州', '白城', '鹤岗', '成都', '海南藏族自治州', '濮阳', '宜昌', '内江', '淮南', '大同',
        '三沙', '武威', '广元', '呼伦贝尔', '曲靖', '赣州', '甘南藏族自治州', '深圳', '铜川', '白银', '肇庆', '湛江', '赤峰', '盘锦', '日照', '衡阳', '随州',
        '石家庄', '延安', '上海', '湖州', '信阳', '鹰潭', '海东地区', '阜新', '焦作', '南平', '芜湖', '安顺', '昭通', '东营', '邢台', '镇江', '昌都地区', '长治',
        '锡林郭勒盟', '晋中', '黔东南苗族侗族自治州', '铁岭', '南通', '果洛藏族自治州', '吴忠', '金华', '阿勒泰地区', '绥化', '汕尾', '南宁', '贺州', '自贡', '北海',
        '玉溪', '景德镇', '绍兴', '珠海', '陇南', '宝鸡', '重庆', '龙岩', '嘉峪关', '柳州', '喀什地区', '阿里地区', '泰安', '保山', '通辽', '阿拉善盟', '烟台',
        '怀化', '东莞', '阳江', '新乡', '滨州', '哈尔滨', '舟山', '莱芜', '娄底', '云浮', '太原', '黔南布依族苗族自治州', '楚雄彝族自治州', '徐州', '大庆', '黄石',
        '桂林', '上饶', '文山壮族苗族自治州', '白山', '西安', '博尔塔拉蒙古自治州', '滁州', '咸宁', '潍坊', '毕节', '克拉玛依', '来宾', '朝阳', '承德', '石嘴山', '江门',
        '惠州', '临沂', '常德', '佛山', '德宏傣族景颇族自治州', '新余', '黄山', '宁德', '丽水', '铜仁', '呼和浩特', '伊春', '贵港', '北京', '那曲地区', '吐鲁番地区',
        '厦门', '嘉兴', '酒泉', '漯河', '南阳', '湘潭', '宜春', '南充', '黔西南布依族苗族自治州', '安康', '三亚', '汉中', '金昌', '宿州', '天津', '日喀则地区',
        '林芝地区', '齐齐哈尔', '山南地区', '安阳', '铜陵', '资阳', '河源', '梧州', '青岛', '澳门特别行政区', '宣城', '迪庆藏族自治州', '伊犁哈萨克自治州', '阿克苏地区',
        '吉安', '福州', '漳州', '怒江傈僳族自治州', '广安', '榆林', '临汾', '巴中', '沈阳', '克孜勒苏柯尔克孜自治州', '张家口', '杭州', '安庆', '和田地区', '昆明',
        '郑州', '荆门', '普洱', '阿坝藏族羌族自治州', '黑河', '大理白族自治州', '盐城', '长春', '凉山彝族自治州', '衢州', '三门峡', '吕梁', '台州', '营口', '淮安',
        '丹东', '驻马店', '六安', '马鞍山', '开封', '三明', '双鸭山', '汕头', '海北藏族自治州', '吉林', '巴音郭楞蒙古自治州', '襄阳', '洛阳', '揭阳', '玉树藏族自治州',
        '十堰', '临夏回族自治州', '商洛', '晋城', '邵阳', '泸州', '济南', '泉州', '莆田', '宁波', '阜阳', '四平', '大连', '葫芦岛', '平顶山', '茂名', '塔城地区',
        '牡丹江', '防城港', '遂宁', '沧州', '宜宾', '甘孜藏族自治州', '中卫', '秦皇岛', '连云港', '河池', '眉山', '苏州', '玉林', '孝感', '延边朝鲜族自治州', '钦州',
        '蚌埠', '遵义', '商丘', '鄂尔多斯', '中山', '包头', '乐山', '济宁', '巴彦淖尔', '雅安', '威海', '渭南', '池州', '保定', '香港特别行政区', '拉萨', '西宁',
        '天水', '红河哈尼族彝族自治州', '淄博', '衡水', '西双版纳傣族自治州', '固原', '百色', '永州', '淮北', '台湾省', '菏泽', '乌鲁木齐', '崇左', '临沧',
        '海西蒙古族藏族自治州', '通化', '忻州', '乌兰察布', '韶关', '抚顺', '兰州', '邯郸', '鸡西', '辽阳', '清远', '佳木斯', '鹤壁', '海口', '泰州', '咸阳', '扬州',
        '南昌', '南京', '周口', '温州', '亳州', '兴安盟', '阳泉', '黄冈', '七台河', '岳阳', '贵阳', '湘西土家族苗族自治州', '张掖', '合肥', '绵阳', '荆州', '聊城',
        '哈密地区', '六盘水', '运城', '梅州', '长沙', '枣庄', '辽源', '常州', '丽江', '松原', '广州', '本溪', '益阳', '攀枝花', '鄂州', '锦州', '武汉', '许昌',
        '萍乡', '庆阳', '乌海', '株洲', '郴州', '德州', '九江', '银川', '宿迁', '朔州', '无锡', '定西', '张家界', '达州', '鞍山', '唐山']

l = []
with open('china_city_geo.json', 'r', encoding='utf-8') as file:
    f = json.load(file)
    d = dict(f)
    for k, v in d.items():
        for i, j in dict(v).items():
            l.append(i)
            print('\'' + i + '\'', ':', [float(j['x']), float(j['y'])], ',')
