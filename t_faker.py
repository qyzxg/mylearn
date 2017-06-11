#!/usr/bin/python
# -*- coding:utf-8 -*-

from faker import Factory
from werkzeug.security import generate_password_hash
import mysql.connector as mc
import random, string, time

fake = Factory.create('zh_CN')

# query = ("SELECT * FROM tags")
# cur.execute(query)
# for (id,name) in cur:
#     print('{},{}'.format(id,name))
citys = ['廊坊市', '黄南藏族自治州', '平凉市', '潮州市州', '抚州市', '德阳市', '昌吉回族自治州', '白城市', '鹤岗市', '成都市', '海南藏族自治州', '濮阳市', '宜昌市', '内江市',
         '淮南市', '大同市',
         '三沙市', '武威市', '广元市', '呼伦贝尔市', '曲靖市', '赣州市', '甘南藏族自治州', '深圳市', '铜川市', '白银市', '肇庆市', '湛江市', '赤峰市', '盘锦市', '日照市',
         '衡阳市', '随州市',
         '石家庄市', '延安市', '上海市', '湖州市', '信阳市', '鹰潭市', '海东地区', '阜新市', '焦作市', '南平市', '芜湖市', '安顺市', '昭通市', '东营市', '邢台市',
         '镇江市', '昌都地区',
         '长治市',
         '锡林郭勒州', '晋中市', '黔东南苗族侗族自治州', '铁岭市', '南通市', '果洛藏族自治州', '吴忠市', '金华市', '阿勒泰地区', '绥化市', '汕尾市', '南宁市', '贺州市',
         '自贡市', '北海市',
         '玉溪市', '景德镇市', '绍兴市', '珠海市', '陇南市', '宝鸡市', '重庆市', '龙岩市', '嘉峪关市', '柳州市', '喀什地区', '阿里地区', '泰安市', '保山市', '通辽市',
         '阿拉善州', '烟台市',
         '怀化市', '东莞市', '阳江市', '新乡市', '滨州市', '哈尔滨市', '舟山市', '莱芜市', '娄底市', '云浮市', '太原市', '黔南布依族苗族自治州', '楚雄彝族自治州', '徐州市',
         '大庆市', '黄石市',
         '桂林市', '上饶市', '文山壮族苗族自治州', '白山市', '西安市', '博尔塔拉蒙古自治州', '滁州', '咸宁市', '潍坊市', '毕节市', '克拉玛依市', '来宾市', '朝阳市', '承德市',
         '石嘴山市',
         '江门市',
         '惠州市', '临沂市', '常德市', '佛山市', '德宏傣族景颇族自治州', '新余市', '黄山市', '宁德市', '丽水市', '铜仁市', '呼和浩特市', '伊春市', '贵港市', '北京市',
         '那曲地区', '吐鲁番地区',
         '厦门市', '嘉兴市', '酒泉市', '漯河市', '南阳市', '湘潭市', '宜春市', '南充市', '黔西南布依族苗族自治州', '安康市', '三亚市', '汉中市', '金昌市', '宿州市',
         '天津市', '日喀则地区',
         '林芝地区', '齐齐哈尔市', '山南地区', '安阳市', '铜陵市', '资阳市', '河源市', '梧州市', '青岛市', '澳门特别行政区', '宣城市', '迪庆藏族自治州', '伊犁哈萨克自治州',
         '阿克苏地区',
         '吉安市', '福州市', '漳州市', '怒江傈僳族自治州', '广安市', '榆林市', '临汾市', '巴中市', '沈阳市', '克孜勒苏柯尔克孜自治州', '张家口市', '杭州市', '安庆市',
         '和田地区', '昆明市',
         '郑州', '荆门市', '普洱市', '阿坝藏族羌族自治州', '黑河市', '大理白族自治州', '盐城市', '长春市', '凉山彝族自治州', '衢州市', '三门峡市', '吕梁市', '台州市', '营口市',
         '淮安市',
         '丹东市', '驻马店市', '六安市', '马鞍山市', '开封市', '三明市', '双鸭山市', '汕头市', '海北藏族自治州', '吉林市', '巴音郭楞蒙古自治州', '襄阳市', '洛阳市', '揭阳市',
         '玉树藏族自治州',
         '十堰市', '临夏回族自治州', '商洛市', '晋城市', '邵阳市', '泸州市', '济南市', '泉州市', '莆田市', '宁波市', '阜阳市', '四平市', '大连市', '葫芦岛市', '平顶山市',
         '茂名市', '塔城地区',
         '牡丹江市', '防城港市', '遂宁市', '沧州市', '宜宾市', '甘孜藏族自治州', '中卫市', '秦皇岛市', '连云港市', '河池市', '眉山市', '苏州市', '玉林市', '孝感市',
         '延边朝鲜族自治州', '钦州市',
         '蚌埠市', '遵义市', '商丘市', '鄂尔多斯市', '中山市', '包头市', '乐山市', '济宁市', '巴彦淖尔市', '雅安市', '威海市', '渭南市', '池州市', '保定市',
         '香港特别行政区', '拉萨市', '西宁市',
         '天水市', '红河哈尼族彝族自治州', '淄博市', '衡水市', '西双版纳傣族自治州', '固原市', '百色市', '永州市', '淮北市', '台湾省市', '菏泽市', '乌鲁木齐市', '崇左市',
         '临沧市',
         '海西蒙古族藏族自治州', '通化市', '忻州市', '乌兰察布市', '韶关市', '抚顺市', '兰州市', '邯郸市', '鸡西市', '辽阳市', '清远市', '佳木斯市', '鹤壁市', '海口市',
         '泰州市', '咸阳市',
         '扬州市',
         '南昌市', '南京市', '周口市', '温州市', '亳州市', '兴安州', '阳泉市', '黄冈市', '七台河市', '岳阳市', '贵阳市', '湘西土家族苗族自治州', '张掖市', '合肥市',
         '绵阳市', '荆州市', '聊城市',
         '哈密地区', '六盘水市', '运城市', '梅州市', '长沙市', '枣庄市', '辽源市', '常州市', '丽江市', '松原市', '广州市', '本溪市', '益阳市', '攀枝花市', '鄂州市',
         '锦州市', '武汉市', '许昌市',
         '萍乡市', '庆阳市', '乌海市', '株洲市', '郴州市', '德州市', '九江市', '银川市', '宿迁市', '朔州市', '无锡市', '定西市', '张家界市', '达州市', '鞍山市',
         '唐山市']
regions = ["北京", "天津", "河北", "山西", "内蒙古", "辽宁", "吉林", "黑龙江 ", "上海", "江苏", "浙江", "安徽", "福建", "江西", "山东", "河南", "湖北 ",
           "湖南", "广东", "广西", "海南", "重庆", "四川", "贵州", "云南", "西藏 ", "陕西", "甘肃", "青海", "宁夏", "新疆", "台湾", "香港", "澳门", "国外 "]
n = 0
m = 0
str_len = 16

while True:
    m += 1
    n += 1
    id = n
    conn = mc.connect(
        user='qyzxg',
        password='qyzxg',
        host='localhost',
        database='blog'
    )

    cur = conn.cursor()
    username = fake.user_name()
    password = generate_password_hash('qyzxg8899')
    email = fake.free_email()
    avatar = fake.file_path(depth=2, category=None, extension='jpg')
    status = random.choice([0, 1])
    is_valid = random.choice([0, 1])
    confirmed = 1
    confirmed_on = fake.date_time_between(start_date="-28d", end_date="now", tzinfo=None)
    created_at = fake.date_time_between(start_date="-28d", end_date="now", tzinfo=None)
    updated_at = fake.date_time_between(start_date="-28d", end_date="now", tzinfo=None)
    last_login = fake.date_time_between(start_date="-28d", end_date="now", tzinfo=None)
    post_total = fake.random_int(min=0, max=999)
    role = random.choice([0, 1])
    wx_img = fake.file_path(depth=2, category=None, extension='jpg')
    zfb_img = fake.file_path(depth=2, category=None, extension='jpg')
    wx_num = random.random() * 10
    zfb_num = random.random() * 10
    city = random.choice(citys)
    county = ''
    ip_addr = fake.ipv4(network=False)
    region = random.choice(regions)
    area = random.choice(['华中', '华南', '华东', '华北', '西部', '东北'])
    country = fake.country()
    cur = conn.cursor()
    ins = (
    "INSERT ignore `users` (`id`, `username`, `password`, `email`, `avatar`, `status`, `is_valid`, `confirmed`, `confirmed_on`, `created_at`, `updated_at`, `last_login`, `post_total`, `role`, `wx_img`, `zfb_img`, `wx_num`, `zfb_num`, `city`, `county`, `ip_addr`, `region`, `area`, `country`) VALUES ({}, '{}', '{}', '{}', '{}', {}, {}, {}, '{}', '{}', '{}', '{}', {}, {}, '{}', '{}', '{:.3}', '{:.3}', '{}', '{}', '{}', '{}', '{}', '{}');".format(
        id, username, password, email, avatar, status, is_valid, confirmed, confirmed_on, created_at, updated_at,
        last_login,
        post_total, role, wx_img, zfb_img, wx_num, zfb_num, city, county, ip_addr, region, area, country))
    cur.execute(ins)
    conn.commit()
    cur.close()
    conn.close()
    print(m, 'ok')
    if n == 300:
        break
    # time.sleep(1)
