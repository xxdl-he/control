import requests
import easygui
import json
import base64
import easygui as g
import time
import sys


name = g.enterbox(msg="输入昵称【不输入默认匿名】", title="sk")
if name:
    pass
else:
    name='匿名'
a = '8bb1b96e9754c1facde5a8901bfe4524'


def ref(full):
    
    req = requests.get(('https://gitee.com/api/v5/repos/xxdlyzbb/xxdlyzbb/contents/chat.json?access_token=' + a))
    b = req.json()
    print(b)
    sha = b['sha']
    u = b['download_url']
    lk = ((requests.get(u)).text)
    ls = lk.split('丨')
    if full:
        pass
    else:
        ls = ls[::-1]
        ls = ls[0:3]
    t = "\n".join(ls)
    
    k = g.textbox(msg=t, title='Chat1.0[Cancel刷新/OK发送/输入t按下OK退出]')
    if k:
        if (k is't'):
            sys.exit()
        t0 = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime())
        meg = (name + '(' + t0 + '):' + k)
        up = lk+'丨'+meg
        meg = base64.b64encode(up.encode("utf-8"))
        io = (str(meg, 'utf8'))
        urlp = 'https://gitee.com/api/v5/repos/xxdlyzbb/xxdlyzbb/contents/chat.json'
        p = {'access_token': a, 'content': io, 'sha': sha,'message': ((((name + '(') + t0) + '):') + k)}
        hh=(requests.put(urlp, json=p).json())
        ref()
    else:
        ref(False)

ref(True)
