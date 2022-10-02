import socket,json,os,platform,time
from urllib.request import urlopen

class hostinfo:
    def getip(self):
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
    def getoutip(self):
        try:
            return json.load(urlopen('http://jsonip.com'))['ip']
        except:
            return "未获取到公网IP"
    def __init__(self):
        print("获取信息中...")
        outip = self.getoutip()
        ip = self.getip()
        print("="*20)
        print("网络信息:")
        print("公网: %s \n内网: %s"%(outip,ip))
        print("="*20)
        print("系统信息:")
        print("系统类型: %s"%platform.system())
        print("系统版本: %s"%platform.version())
        print("计算机名字: %s"%platform.node())
        print("CPU架构: %s"%platform.machine())
        print("CPU厂商: %s"%platform.processor())
        print("系统时间: %s"%time.asctime())
        print("="*20)
        print("脚本信息:")
        print("脚本位置: %s"%os.path.split(os.path.realpath(__file__))[0].replace(r"moligeek\core\network",''))
        print("="*20)
if __name__ == "__main__":
    a = hostinfo()