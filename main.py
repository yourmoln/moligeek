import sys
import os
from socket import gethostbyname
script_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(script_path)
from moligeek import *

<<<<<<< HEAD
ssl = input("是否为https://\n[1]是\n[2]否\n")
if ssl in ["是", "1"]:
    ssl = "https://"
elif ssl in ["否", "2"]:
    ssl = "http://"
else:
    print("未选择，默认为是")
    ssl = "https://"
name = input("请输入链接:"+ssl)
url = ssl+name

try:
    print("域名",name,"IP："+gethostbyname(name)+"(仅供参考)")
except:
    print("Warning: 当前域名检测不到IP可能无法进行进行操作")

mode = input("请选择模式:\n[1]下载源码\n[2]ping\n[3]获取ip\n[4]提交表单\n[5]后台扫描\n[6]洪水攻击\n")
=======
mainmode = input("请选择模式:\n[1]web\n[2]network\n")
if mainmode in ["1", "web"]:
    ssl = input("是否为https://\n[1]是\n[2]否\n")
    if ssl in ["是", "1"]:
        ssl = "https://"
    elif ssl in ["否", "2"]:
        ssl = "http://"
    else:
        print("未选择，默认为是")
        ssl = "https://"
    name = input("请输入链接:"+ssl)
    url = ssl+name
    mode = input("请选择模式:\n[1]下载源码\n[2]获取ip\n[3]提交表单\n[4]后台扫描\n[5]洪水攻击\n")
    # 判断模式
    if mode in ["1", "获取源码"]:
        web.getsrc(url)
    if mode in ["2", "获取ip"]:
        network.getip(name)
    if mode in ["3", "提交表单"]:
        web.upform(url)
    if mode in ["4", "后台扫描"]:
        web.findadmin(url)
    if mode in ["5", "洪水攻击"]:
        network.startattack(url)
        
if mainmode in ["2", "network"]:
    target_ip = input("请输入目标ip:")
    mode = input("请选择模式:\n[1]ddos\n[2]ping\n")
>>>>>>> 5458b475586d0d184e6acb0c2026184edd26d6d6



    if mode in ["1", "ddos"]:
        network.ddos_attack(target_ip)
    if mode in ["2", "ping"]:
        network.ping(target_ip)