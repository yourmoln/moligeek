#by yourmoln
from socket import socket
import threading
from threading import Lock,Thread

import requests
import os
from socket import gethostbyname

#全局变量
s=0
f=0

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
mode=input("请选择模式:\n(1)下载源码\n(2)ping\n(3)获取ip\n(4)提交表单\n(5)后台扫描\n")

#获取源码并写入
def getsrc():
    try:
        response=requests.get(url,headers)
        response.encoding="utf–8"
        print(response.text)
        pathname = name.replace("/","_")
        srcpath=path+"/src/"+pathname+".txt"
        with open(srcpath,"w+") as f:
            f.write(response.text)
        print("成功写入文件，文件路径:"+srcpath)
    except:
        print("写入失败\n请检查网络是否正常或网页是否存在")

#ping
def ping():
    os.system("ping "+name)

#获取ip
def getip():
    try:
        print("ip:"+gethostbyname(name))
    except:
        print("未检测到ip\n请检查网络是否正常或域名是否正确")

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
        post()
    elif method in ["2","get"]:
        get()
    else:
        post()

#后台文件扫描
def findadmin():
    global s
    global f
    kind=input("请选择后台语言类型\n[1]ASP\n[2]ASPX\n[3]DIR\n[4]JSP\n[5]MDB\n[6]PHP\n默认为php\n")
    if kind in ["1","ASP","asp"]:
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
        kind="PHP.txt"
    with open(path+"/set/"+kind,"rt",encoding='gbk') as f:
        txt=f.read()
    txtlist=txt.split("\n")
    s=0
    f=0
    num=len(txtlist)
    for i in txtlist:
        print("\r进度("+str(s+f)+"/"+str(num)+")",end="")
        t1 = threading.Thread(target=shaomiao,args=(i,))
        t1.start()
        


    print("总扫描"+str(s+f)+"个页面，成功检测"+str(s)+"个页面")
    
def shaomiao(i):
    global s
    global f
    try:
        txturl=url+i
        r=requests.get(txturl,headers)
        if r.status_code==requests.codes.ok:
            print(txturl)
            s=s+1
        else:
            f=f+1
    except:
        f=f+1
    
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
    
    
def post():
    try:
        response = requests.post(url, data=formdata)
        response.encoding="utf–8"
        print(response.text)
    except:
        print("发送失败\n请检查网络是否正常或页面是否存在")
        
def get():
    try:
        response = requests.get(url, params=formdata)
        response.encoding="utf–8"
        print(response.text)
    except:
        print("发送失败\n请检查网络是否正常或页面是否存在")
