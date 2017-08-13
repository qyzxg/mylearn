import requests
import base64
from PIL import Image




session = requests.Session()
code_url = 'http://www.lvyouquan.com/CheckCode.aspx'
code_r = session.get(code_url)
with open('imgout.gif', 'wb') as code:
    code.write(code_r.content)

im = Image.open('imgout.gif')
im.show()


# headers = {
#     'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8',
#     'Accept-Encoding': 'gzip, deflate',
#     'Accept-Language': 'zh-CN,zh;q=0.8',
#     'Cache-Control': 'max-age=0',
#     'Connection': 'keep-alive',
#     'Content-Length': '463',
#     'Content-Type': 'application/x-www-form-urlencoded',
#     'Cookie': 'SERVERID=web131; LyqSessionId=eo112z4uziw03kgyxgdjvatv; CurrentBrowserId=5139b176-1782-4324-9cda-468372f17fb0; BusinessCURRENTSUBSTATION#=10; PUBLICBUSINESSSTARTCITY#=10; ArticleIdCookie=8b43246a9c5547339f8c834d9f747c13; _qddamta_4001003258=3-0; PPK.Login.MD5Password=45ff3b4a0eae06dffc8d060b0dab127c; CancelValideCode=1; Hm_lvt_c0b9052fe198c2e1c22a7f1bd537393d=1502590019; Hm_lpvt_c0b9052fe198c2e1c22a7f1bd537393d=1502599271; _ga=GA1.2.158585555.1502590019; _gid=GA1.2.749974139.1502590019; _qddaz=QD.auoxk9.3xsurm.j6a3avac; _qdda=3-1.3gilhn; _qddab=3-jjnrh2.j6a8rf7w; ShowIndexQuanxiaoErClass=0',
#     'DNT': '1',
#     'Host': 'www.lvyouquan.com',
#     'Origin': 'http://www.lvyouquan.com',
#     'Referer': 'http://www.lvyouquan.com/NewIndex.aspx',
#     'Upgrade-Insecure-Requests': '1',
#     'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Ubuntu Chromium/60.0.3112.78 Chrome/60.0.3112.78 Safari/537.36',
# }
code_input = input('请输入验证码：')
data = {
    '__VIEWSTATE': '/wEPDwULLTIxNDc0NTA2MTlkZNHrdofqnL5dhFcuVIbnFCCuR8/k',
    '__VIEWSTATEGENERATOR': '63A21F34',
    '__EVENTVALIDATION': '/wEdAAg4hn5z4jt5ne1ewAHtNztS/w7FBQM+wGpthaD+GJC7HJABr1TwJsCCOlEaLDdTzUJjemWCTRgEB59HPczIGVNwdjb4xzpKucCqKjegIpvFhvV1P2O9fdNQDbgDMbkOS0fN+DvxnwFeFeJ9MIBWR693Ng/6JFdLUYz5JnkUUQCS1u1QTxU+0t4o/nlcbzKlVc7k7Zjv',
    'txtUserName': 'pzx4@qq.com',
    'txtPassword': 'Answer',
    'txtCheckCode': code_input,
    'Button1': '登录',
}
r = session.post('http://www.lvyouquan.com/NewIndex.aspx', data=data)

print(r.text)


