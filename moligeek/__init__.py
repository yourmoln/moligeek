# -*- coding: utf-8 -*-
# by yourmoln

import sys
import os
script_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(script_path)
import path_dict
import core
print(core.__docs__)

for _ in range(3):
    try:
        import requests
        import meo
        import bs4
        break
    except:
        source_list = [
            "https://pypi.douban.com/simple",
            "https://pypi.org/simple"
        ]
        print("有缺失的包，请选择一种下载方式: ")
        print("\n".join([
            f"[{i + 1}] {source}"
            for i, source in enumerate(source_list)
        ]))
        idx = int(input("请输入序号(推荐使用1): ")) - 1
        requirements_path = os.path.join(script_path, "../requirements.txt")
        os.system(
            f"python -m pip install -r {requirements_path} -i {source_list[idx]}"
        )
        print("\a安装完成，开始运行")

import core.network as network
import core.web as web
import core.zip as zip


#检查网络，一言
print("检查网络中......")
try:
    response = requests.get('https://api.ixiaowai.cn/api/ylapi.php')
    response.encoding = "utf–8"
    meo.screen.blue_font('一言:'+response.text)
except:
    meo.screen.red_font("\a网络异常,请检查网络是否连接,若你的网络没有问题，请忽略此提示")