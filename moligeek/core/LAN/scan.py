import os
import threading
from pythonping import ping
import socket
from core.network import Hostinfo

class Scan:
    """子网扫描"""

    def __init__(self, range:str = ".".join(Hostinfo.getip().split(".")[:-1]) ):
        self.range = range
        self.ip_list = []
    def scan_device(self,ip):
        response = ping(ip, count=1, timeout=1)
        if response.success():
            try:
                hostname = socket.gethostbyaddr(ip)[0]
            except Exception:
                hostname = "未知设备"
            self.ip_list.append([ip, hostname])
    def run(self) -> list:
        """多线程扫描"""
        # Create a list of threads
        threads = []
        # Scan
        for i in range(1, 255):
            ip = self.range + "." + str(i)
            t = threading.Thread(target=self.scan_device, args=(ip,))
            threads.append(t)
            t.start()
        # Wait for all threads to complete
        for t in threads:
            t.join()
        return self.ip_list


if __name__ == "__main__":
    a = Scan(range="192.168.31")
    for i in a.run():
        print(i)
    print("扫描完成")