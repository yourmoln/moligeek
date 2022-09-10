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