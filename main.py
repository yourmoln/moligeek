if __name__ =='__main__':

    import sys
    import os
    script_path = os.path.split(os.path.realpath(__file__))[0]
    sys.path.append(script_path)
    from moligeek import *

    mainmode = input("请选择模式:\n[0]本机信息\n[1]web\n[2]network\n[3]LAN\n[4]密文处理\n[5]压缩包破解\n")
    if mainmode in ["0", "本机信息"]:
        hostinfo = network.hostinfo()
    elif mainmode in ["1", "web"]:
        ssl = input("是否为https://\n[1]是\n[2]否\n")
        if ssl in ["是", "1"]:
            ssl = "https://"
        elif ssl in ["否", "2"]:
            ssl = "http://"
        else:
            print("未选择，默认为是")
            ssl = "https://"
        name = input("请输入链接:"+ssl)
        url = ssl+name
        mode = input("请选择模式:\n[1]下载源码\n[2]获取ip\n[3]提交表单\n[4]后台扫描\n[5]洪水攻击\n")
        # 判断模式
        if mode in ["1", "获取源码"]:
            web.getsrc(url)
        if mode in ["2", "获取ip"]:
            network.getip(name)
        if mode in ["3", "提交表单"]:
            web.upform(url)
        if mode in ["4", "后台扫描"]:
            web.findadmin(url)
        if mode in ["5", "洪水攻击"]:
            network.startattack(url)
            
    elif mainmode in ["2", "network"]:
        target_ip = input("请输入目标ip:")
        mode = input("请选择模式:\n[1]泛洪攻击\n[2]ping\n[3]洪攻击\n")

        if mode in ["1", "泛洪攻击"]:
            network.ddos_attack(target_ip)
        if mode in ["2", "ping"]:
            network.ping(target_ip)
        if mode in ["3", "洪攻击"]:
            network.ping(target_ip)

    elif mainmode in ["3", "LAN"]:
        mode = input("请选择模式:\n[1]设备扫描\n")

        if mode in ["1", "设备扫描"]:
            range = input("请输入扫描范围\n例:192.168.1\n")
            print("扫描中...")
            scan = LAN.scan(range)

    elif mainmode in ["4", "密文处理"]:
        codetext = input("请输入文本:")
        mode = input("请选择模式:\n[1]一键解密\n[2]栅栏解密\n")
        if mode in ["1", "一键解密"]:
            encode = encode.todecode(codetext)
        if mode in ["2", "栅栏解密"]:
            textlengh = int(input("每组字数:"))
            print(encode.fence.decrypt(codetext, textlengh))

    elif mainmode in ["5", "压缩包破解"]:
        zip_path = input("请输入压缩包路径:")
        mode = input("请选择破解模式:\n[1]纯数字\n[2]数字字母混合\n[3]数字字母符号混合\n")
        if mode in ["1", "纯数字"]:
            zip.zipkey(zip_path,0)
        if mode in ["2", "数字字母混合"]:
            zip.zipkey(zip_path,1)
        if mode in ["3", "数字字母符号混合"]:
            zip.zipkey(zip_path,2)
    if os.name == "nt":
        input("按回车键结束程序")
