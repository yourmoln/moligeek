import os
import threading
import subprocess
from core.network import Hostinfo

class Scan:
    """子网扫描"""

    def __init__(self, range:str = ".".join(Hostinfo.getip().split(".")[:-1]) ):
        self.range = range
        self.ip_list = []
        if os.name == "nt":
            def scan_device(ip):
                address = ip
                result = subprocess.run(["ping", "-n", "1", address], capture_output=True, text=True)
                response = result.stdout
                if "ttl" in response.lower():
                    self.ip_list.append(address)
        else:
            def scan_device(ip):
                address = ip
                result = subprocess.run(["ping", "-c", "1", address], capture_output=True, text=True)
                response = result.stdout
                if "ttl" in response.lower():
                    self.ip_list.append(address)
        self.ping = scan_device

    def run(self) -> list:
        """多线程扫描"""
        # Create a list of threads
        threads = []
        # Scan
        for i in range(1, 255):
            ip = self.range + "." + str(i)
            t = threading.Thread(target=self.ping, args=(ip,))
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