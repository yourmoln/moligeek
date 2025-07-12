import socket,json,os,platform,time
from requests import get

class Hostinfo:
    """获取本机信息"""
    @staticmethod
    def getip():
        """获取内网ip"""
        ip = None
        port = None
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            address = ("8.8.8.8", 80)
            s.connect(address)
            sockname = s.getsockname()
            ip = sockname[0]
            port = sockname[1]
        finally:
            s.close()
        return ip
    @staticmethod
    def getoutip():
        """获取公网ip"""
        try:
            return get('http://ifconfig.me/ip', timeout=1).text.strip()
        except:
            return None
    def all(self) -> dict:
        """获取所有信息"""
        result = {"网络信息":{"公网ip":self.outip,"内网ip":self.ip},
                  "系统信息":{"系统类型":platform.system(),
                                "系统版本":platform.version(),
                                "计算机名":platform.node(),
                                "CPU架构":platform.machine(),
                                "CPU厂商":platform.processor(),
                                "系统时间":time.asctime()},
                  "脚本信息":{"脚本位置":os.path.split(os.path.realpath(__file__))[0].replace(r"moligeek\core\network",'')}}
        return result
    def __init__(self):
        self.outip = self.getoutip()
        self.ip = self.getip()
if __name__ == "__main__":
    print("获取信息中...")
    a = Hostinfo()
    result = a.all()
    for key,value in result.items():
        print("="*20)
        print(key)
        for k,v in value.items():
            print(k,v)
