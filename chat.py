import requests
import easygui
import json
import base64
import easygui as g
import time
import sys


user_info = []
user_info = g.multpasswordbox('请完成启动配置','SK',("昵称【空即匿名】","显示消息数"))
name = user_info[0]
mu=user_info[1]
if mu:
    mu=int(mu)
else:
    mu=5
mut=str(mu)
if name:
    pass
else:
    name = '匿名'
a = '8bb1b96e9754c1facde5a8901bfe4524'


def ref(full):

    req = requests.get(
        ('https://gitee.com/api/v5/repos/xxdlyzbb/xxdlyzbb/contents/chat.json?access_token=' + a))
    b = req.json()
    print(b)
    sha = b['sha']
    u = b['download_url']
    lk = ((requests.get(u)).text)
    ls = lk.split('丨')
    if full:
        if (len(ls) >= mu):
            title = ('【'+name+'】最新'+mut+'条')
            ls = ls[::-1]
            ls = ls[0:mu]
            ls = ls[::-1]
        else:
            title = ('【'+name+'】顺序全部')
    else:
        ls = ls[::-1]
        ls = ls[0:mu]
        ls = ls[::-1]
        title = ('【'+name+'】最新'+mut+'条')
    t = "\n".join(ls)
    k = g.textbox(msg=t, title='Chat1.0[C刷新/O发送/关命令行退出]→'+title)
    if k:
        if (k is 't'):
            sys.exit()
        t0 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        meg = (name + '(' + t0 + '):' + k)
        up = lk+'丨'+meg
        meg = base64.b64encode(up.encode("utf-8"))
        io = (str(meg, 'utf8'))
        urlp = 'https://gitee.com/api/v5/repos/xxdlyzbb/xxdlyzbb/contents/chat.json'
        p = {'access_token': a, 'content': io, 'sha': sha,
             'message': ((((name + '(') + t0) + '):') + k)}
        hh = (requests.put(urlp, json=p).json())
        ref(False)
    else:
        ref(False)


ref(True)
