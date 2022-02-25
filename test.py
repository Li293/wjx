from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import *
import sys
from aip import AipOcr
import win32gui
import requests
import re
import time
import random
import execjs

def get_infor(img):
    APP_ID = '23589367'
    API_KEY = 'cVOtt7wQtwDXIdh38kEtizAG'
    SECRET_KEY = 'Brul9on20orcnT23aGERxcjtqiGfkfFQ'
    client = AipOcr(APP_ID, API_KEY, SECRET_KEY)
    res = client.basicGeneral(img)
    infor= res.setdefault('words_result', [{'words': 0}])
    return infor

hwnd = win32gui.FindWindow(None, '群聊')
app = QApplication(sys.argv)

wjx_url=''

while wjx_url=='':

    screen = QApplication.primaryScreen()
    img = screen.grabWindow(hwnd).toImage()
    img.save("screenshot.jpg")
    with open('screenshot.jpg','rb')as fp:
        infor=get_infor(fp.read())

    for i in infor:
        if 'https://www.wjx.cn' in i['words']:
            wjx_url=i['words']
            nowtime=time.time()
url=wjx_url
data={'submitdata': '1$1}2$姓名}3$学号'}

head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69',
        'Accept': 'text/plain, */*; q=0.01',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9,en;q=0.8,en-GB;q=0.7,en-US;q=0.6',
        'Cache-Control': 'no-cache',
        'Connection': 'keep-alive',
        'Content-Length': '24',
        'Content-Type': 'application/x-www-form-urlencoded; charset=UTF-8',
        'Cookie': '.ASPXANONYMOUS=ANHY-BtG2AEkAAAANzNlZDUxZjEtM2NhYS00MGMzLTk2NTAtMDA2MjE1MWQwOGMyKHqo6oDF_m7dQ4FecaqfgtEtYeI1; UM_distinctid=17e81b91a7a8d-0e5236a782b8d8-5e181856-e1000-17e81b91a7b1ad; Hm_lvt_21be24c80829bd7a683b2c536fcf520b=1642853899,1642902003; CNZZDATA4478442=cnzz_eid%3D640470053-1626665396-%26ntime%3D1642902078; wjxawardload=8290%7C148018840; jac148018840=98950827; acw_tc=781bad0a16429060002035463e023331c1cacf995985232e3ab41d8a19c547; jac124883360=80112309; SERVERID=0f3eb8fcde19feef85b46d49c555413b|1642906035|1642902001; Hm_lpvt_21be24c80829bd7a683b2c536fcf520b=1642906037; ssxmod_itna=YuitAI8tBIx+xBPGKgq7unDGgUxuCZ1jPZG740yureGzDAxn40iDtPoNxGTg09+=M7m+n5TqSpR2Iaok9G7TsrDCPGnDB9vxr9Pxii9DCeDIDWeDiDG4GmR4GtDpxG=Djm/ZCSLxYPGWbqGfDDoDY362DitD4qDBGg3DKqGgbM+sbu0LWWtohMqqsBhnD0t3xBLqi1wnCQcayDNqq1WOKB4DCgvCs7w=RpxU/BXWKqGytKGuATUlRbRCOTXS/d+xIYPjw0vXt7pNz7v4IDmQA7WU7YwsrfDKBx/d/b+bf5DAla4SPD==; ssxmod_itna2=YuitAI8tBIx+xBPGKgq7unDGgUxuCZ1jPZGDnK8rxDtDlZCCxjR0y5ZcPT2didBAZMx65NDzE005TQ+lyDvVfZBq05kKFPS2hqz/bdrk1+Zc9c2PXoIE=mPc8ZQgNQzxIQIu8ZovK7RrdlDnvE34KZ3+N0Ikw/bdRol22RzEPkjOG7C35Ez2o6UYNwAgGYh20Ypr=T64N6C+GiNcALR2Eo3colR=08LxIqnhKleKB87GKsFzEhqnYYLEf1sYuxIuvQsDQ8gzOYzEfNwwIRdpBj1qZ+W5b6istk91z/+RWWc4Qs05Q7YuCYaiA2/iczQ4DZ42IDzA4=IcDZ9EDbt3+qxnZDn5BmZb0dzI=la=Y0gYax3ReleE/0blRq3neNmst5zYFrYa93940mI0uRbnd450UORzcnnnoKygGTNayaf2vGmvUnGUWKVTxPOmFvpS38B71lKmDnDYc8D9+DFKdmFgq8gOrYuS3dlzuQixDKujflPs7WAnK60kO7HsDvP7sq/WVOWb=pQAPmPvN/Wm1tdAIth5T9YO/tu4aOx+5YTW+s5B3zO4pK+307qDDLxD29GDD===',
        'Host': 'www.wjx.cn',
        'Origin': 'https://www.wjx.cn',
        'Pragma': 'no-cache',
        'Referer': url,
        }

def get(url):
    try:
        head={'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4692.99 Safari/537.36 Edg/97.0.1072.69'}
        r=requests.get(url,timeout=30,headers=head)
        r.raise_for_status()
        r.encoding=r.apparent_encoding
        return r
    except:
        return '产生异常'
def starttimechange(starttime):
    start_time=''
    for i_time in starttime:
        if i_time=='/':
            start_time=start_time+'%2F'
        elif i_time==' ':
            start_time=start_time+'%20'
        elif i_time==':':
            start_time=start_time+'%3A'
        else:start_time=start_time+i_time
    return start_time
def get_jqsign(ktimes,jqnonce):
    result = []
    b = ktimes % 10
    if b == 0:
        b = 1
    for char in list(jqnonce):
        f = ord(char) ^ b
        result.append(chr(f))
    return ''.join(result)
ct = execjs.compile("""
function DecodeId(input) {
            return input ^ 2130030173;
        }
""")
urltxt=get(url).text
activiteid1=re.findall('var activityId =(.*?);',urltxt)[0]
activiteid=ct.call("DecodeId",activiteid1)

ctx = execjs.compile("""
function abcd1(_0x17164c) {
  return abcd2(_0x17164c, 3597397);
}
function abcd2(_0x1b1e02, _0x23f273) {
  if (!abcdx()) {
    return;
  }
  var _0x1f9ba1 = 2147483648;
  var _0x3b83ae = 2147483647;
  var _0x4ad458 = ~~(_0x1b1e02 / _0x1f9ba1);
  var _0x470088 = ~~(_0x23f273 / _0x1f9ba1);
  var _0x5bc159 = _0x1b1e02 & _0x3b83ae;
  var _0x35dfa5 = _0x23f273 & _0x3b83ae;
  var _0x353774 = _0x4ad458 ^ _0x470088;
  var _0x4a742c = _0x5bc159 ^ _0x35dfa5;
  return _0x353774 * _0x1f9ba1 + _0x4a742c;
}
function abcd3(_0x420610, _0x1b425f) {
  if (_0x420610 - 62 < 0) {
    var _0xea36a8 = _0x1b425f["substr"](_0x420610, 1);
    return _0xea36a8;
  }
  var _0x45571c = _0x420610 % 62;
  var _0x4e6181 = parseInt(_0x420610 / 62);
  return abcd3(_0x4e6181, _0x1b425f) + _0x1b425f["substr"](_0x45571c, 1);
}
function abcd4(_0x11dbf0, _0x1558df) {
  if (!abcdx()) {
    return;
  }
  var _0x556c7b = _0x1558df["split"]("");
  var _0x27312b = _0x1558df["length"];
  for (var _0x107cfb = 0; _0x107cfb < _0x11dbf0["length"]; _0x107cfb++) {
    var _0x410c33 = parseInt(_0x11dbf0[_0x107cfb]);
    var _0x43a652 = _0x556c7b[_0x410c33];
    var _0x433a77 = _0x556c7b[_0x27312b - 1 - _0x410c33];
    _0x556c7b[_0x410c33] = _0x433a77;
    _0x556c7b[_0x27312b - 1 - _0x410c33] = _0x43a652;
  }
  _0x1558df = _0x556c7b["join"]("");
  return _0x1558df;
}
function abcd5(_0x5565b6) {
  if (!abcdx()) {
    return;
  }
  var _0x546e81 = 0;
  var _0x5ed7b1 = _0x5565b6["split"]("");
  for (var _0x28a6c3 = 0; _0x28a6c3 < _0x5ed7b1["length"]; _0x28a6c3++) {
    _0x546e81 += _0x5ed7b1[_0x28a6c3]["charCodeAt"]();
  }
  var _0x5af006 = _0x5565b6["length"];
  var _0x5258e0 = _0x546e81 % _0x5af006;
  var _0x2b24c5 = [];
  for (var _0x28a6c3 = _0x5258e0; _0x28a6c3 < _0x5af006; _0x28a6c3++) {
    _0x2b24c5["push"](_0x5ed7b1[_0x28a6c3]);
  }
  for (var _0x28a6c3 = 0; _0x28a6c3 < _0x5258e0; _0x28a6c3++) {
    _0x2b24c5["push"](_0x5ed7b1[_0x28a6c3]);
  }
  return _0x2b24c5["join"]("");
}
function abcdu(_0x92722d) {
  var _0x2eb3ad = -480;
  var _0x3a4ef4 = new Date()["getTimezoneOffset"]();
  var _0x58cdae = _0x2eb3ad - _0x3a4ef4;
  return _0x92722d["getTime"]() / 1000 + _0x58cdae * 60;
}
function abcdx() {
  return true;
}
function get_jqParam(rndnum, initstime, activityId) {
  var _0x3098bf = rndnum["split"](".")[0]; // rndnum from html
  var _0x4aaf4a = abcd1(parseInt(_0x3098bf));
  var _0x149db2 = (_0x4aaf4a + "")["split"]("");
  var _0x5b9ae2 = initstime; //"2021/1/28 17:36:28"
  var _0x4eae39 = abcdu(new Date(_0x5b9ae2["replace"](new RegExp("-", "gm"), "/")));
  var _0x5050a2 = _0x4eae39 + "";
  if (_0x4eae39 % 10 > 0) {
    _0x5050a2 = _0x5050a2["split"]("")["reverse"]()["join"]("");
  }
  var _0xd16fcc = parseInt(_0x5050a2 + "89123");
  var _0x149db2 = (_0xd16fcc + "" + (_0x4aaf4a + ""))["split"]("");
  var _0x1b3de6 = abcd4(_0x149db2, "kgESOLJUbB2fCteoQdYmXvF8j9IZs3K0i6w75VcDnG14WAyaxNqPuRlpTHMrhz");
  var _0x3a5cf2 = _0xd16fcc + _0x4aaf4a + parseInt(activityId);
  jqParam = abcd3(_0x3a5cf2, _0x1b3de6);
  var _0x5d90fd = abcd5(jqParam);
  return jqParam
}
""")

def get_jqpram(rn,starttime1,activiteid):
    jqpram1 = ctx.call("get_jqParam", rn, starttime1, activiteid)
    asc_value = 0
    for i in jqpram1:
        asc_value += ord(i)

    start_location = asc_value % len(jqpram1)
    e = ''
    for j in range(len(jqpram1)):
        c = start_location + j
        if c >= len(jqpram1):
            c -= len(jqpram1)
        e += jqpram1[c]
    return e

def submit(url,data):
    urltxt = get(url).text
    shortid=url.split('/')[-1].split('.')[0]
    starttime1 = re.search(r'\d+?/\d+?/\d+?\s\d+?:\d+?:\d',urltxt).group()
    starttime=starttimechange(starttime1)
    source='directphone'
    submittype=1
    ktime=random.randint(15,50)
    hlv=1
    rn= re.search(r'\d{9,10}\.\d{8}',urltxt)[0]
    t='{}{}'.format(int(time.time()), random.randint(100, 200))
    jqnonce=re.search(r'.{8}-.{4}-.{4}-.{4}-.{12}',urltxt)[0]
    jqsign=get_jqsign(ktime,jqnonce)
    jqpram=get_jqpram(rn,starttime1,activiteid)
    fin_url="https://www.wjx.cn/joinnew/processjq.ashx?shortid="+shortid+"&starttime="+starttime+"&source=directphone&submittype="+str(submittype)+'&ktimes='+str(ktime)+'&hlv='+str(hlv)+'&rn='+rn+'&jqpram='+jqpram+'&t='+t+'&jqnonce='+jqnonce+'&jqsign='+jqsign;
    r=requests.post(fin_url, headers=head,data=data)
    return r.text

infor = submit(url, data)
while infor == 22:
    time.sleep(0.5)
    infor = submit(url, data)
print(infor)

print(str(time.time()-nowtime))
