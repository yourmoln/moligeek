if __name__ =='__main__':

    import sys
    import os
    import threading
    script_path = os.path.split(os.path.realpath(__file__))[0]
    sys.path.append(script_path)
    from moligeek import *
    start = start()
    mainmode = input("请选择模式:\n[0]本机信息\n[1]web\n[2]network\n[3]LAN\n[4]密文处理\n[5]压缩包破解\n")
    if mainmode in ["0", "本机信息"]:
        print("获取信息中...")
        a = network.Hostinfo()
        result = a.all()
        for key,value in result.items():
            print("="*20)
            print(key)
            for k,v in value.items():
                print(k,v)
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
            src = web.getsrc(url)
            print(f"已写入文件{src}") if src != None else print("获取失败")
        if mode in ["2", "获取ip"]:
            print(f"ip:{network.getip(name)}")
        if mode in ["3", "提交表单"]:
            formname = formvalue = []
            formdata = {}
            method = input("请选择方法:\n[1]post\n[2]get\n不作选择默认为post\n")
            n = int(input("请选择提交数量:"))
            for i in range(n):
                formname += [input("请输入第"+str(i+1)+"个变量名:")]
                formvalue += [input("请输入第"+str(i+1)+"个变量值:")]
            for i in range(n):
                formdata[formname[i]] = formvalue[i]
            result = web.upform(url,method = method,formdata = formdata)
            print(result) if result != None else print("提交失败")
        if mode in ["4", "后台扫描"]:
            kind = input("请选择后台语言类型\n[0]全部\n[1]ASP\n[2]ASPX\n[3]DIR\n[4]JSP\n[5]MDB\n[6]PHP\n默认为全部\n")
            print("扫描中，将在扫描结束后显示结果")
            result = web.findadmin(url, kind = kind)
            for i in result:
                print(i)
        if mode in ["5", "洪水攻击"]:
            try:
                speed = int(input("请输入攻击速度(小心卡死自己):"))
                speed = speed if speed > 0 else 10
            except:
                print("设置错误，默认为10")
                speed = 10
            a = network.Attack(url,speed)
            t = threading.Thread(target=a.startattack, args=())
            t.start()
            while True:
                print("\r已发送{}个包，失效{}个包".format(
                a.collector['success'] + a.collector['err'],
                a.collector['err']
            ), end="")
    elif mainmode in ["2", "network"]:
        target_ip = input("请输入目标ip:")
        mode = input("请选择模式:\n[1]泛洪攻击\n[2]洪攻击\n[3]ping\n")

        if mode in ["1", "泛洪攻击"]:
            print("\033[31m注意！此功能极有可能耗尽你的宽带\033[0m")#红色字体
            port = int(input("请输入起始端口:"))
            d = network.Ddos(target_ip, port = port)
            t = threading.Thread(target=d.all, args=())
            t.start()
            while True:
                print ("\r已发送 %s 个包到 %s 通过端口:%s"%(d.data['sent'],d.ip,d.data['port']),end="")
        if mode in ["2", "洪攻击"]:
            print("\033[31m注意！此功能极有可能耗尽你的宽带\033[0m")#红色字体
            port = int(input("请输入目标端口:"))
            d = network.Ddos(target_ip, port = port)
            t = threading.Thread(target=d.one, args=())
            t.start()
            while True:
                print ("\r已发送 %s 个包到 %s 通过端口:%s"%(d.data['sent'],d.ip,d.port),end="")
        if mode in ["3", "ping"]:
            print("pinging...")
            print(network.ping(target_ip))
    elif mainmode in ["3", "LAN"]:
        mode = input("请选择模式:\n[1]设备扫描\n")

        if mode in ["1", "设备扫描"]:
            range = input("请输入扫描范围\n例:192.168.1\n")
            print("扫描中...")
            scan = LAN.Scan(range = range)
            for i in scan.run():
                print(i)
            print("扫描完成")
    elif mainmode in ["4", "密文处理"]:
        codetext = input("请输入文本:")
        mode = input("请选择模式:\n[1]一键解密\n[2]栅栏解密\n")
        if mode in ["1", "一键解密"]:
            dc = encode.todecode(codetext)
            result = dc.autodecode()
            print("解密结果如下")
            for key, value in result.items():
                if value is not None:
                    print(key, value)
        if mode in ["2", "栅栏解密"]:
            textlengh = int(input("每组字数:"))
            print(encode.fence.decrypt(codetext, textlengh))

    elif mainmode in ["5", "压缩包破解"]:
        zip_path = input("请输入压缩包路径:")
        mode = input("请选择破解模式:\n[1]纯数字\n[2]数字字母混合\n[3]数字字母符号混合\n")
        if mode in ["1", "纯数字"]:
            print(zip.zipkey(zip_path,0))
        if mode in ["2", "数字字母混合"]:
            print(zip.zipkey(zip_path,1))
        if mode in ["3", "数字字母符号混合"]:
            print(zip.zipkey(zip_path,2))
    if os.name == "nt":
        input("按回车键结束程序")
