import os
import socket,subprocess
from concurrent.futures import ThreadPoolExecutor
from core.network import Hostinfo

class Scan:
    """子网扫描"""

    def __init__(self, range:str = ".".join(Hostinfo.getip().split(".")[:-1]) ):
        self.range = range
        self.ip_list = []
        self.m = '-n' if os.name == 'nt' else '-c'
    def scan_device(self,ip):
        cmd = ["ping", self.m, "1", ip]
        result = subprocess.run(cmd, capture_output=True, text=True)
        response = result.stdout
        if "ttl" in response.lower():
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except Exception:
                hostname = "未知设备"
            self.ip_list.append([ip, hostname])
    def run(self) -> list:
        """线程池扫描"""
        with ThreadPoolExecutor(max_workers=256) as executor:
            ips = [self.range + "." + str(i) for i in range(255)]
            executor.map(self.scan_device, ips)
        return self.ip_list


if __name__ == "__main__":
    a = Scan(range="192.168.31")
    for i in a.run():
        print(i)
    print("扫描完成")