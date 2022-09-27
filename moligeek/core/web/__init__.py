import re
import meo
import requests
import threading
import sys
import os
script_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(script_path, "../../"))
import path_dict

from .imitate import Imitate

HOST_PATTERN = r".+://(.+)"
headers = {
    "User-Agent": meo.net.UserAgent.FIREFOX.value
}


def getsrc(url, output=None, headers=headers):
    host_match = re.match(HOST_PATTERN, url)
    host = host_match.group(1)
    try:
        response = requests.get(url, headers)
        response.encoding = "utf–8"
        print(response.text)
        fname = host.replace("/", "_")
        if output is None:
            output = f"./output/{fname}"
        meo.to_file(output, response.text)
        print("\a成功写入文件，文件路径:"+output)
    except:
        print("\a写入失败\n请检查网络是否正常或网页是否存在")


def post(url, data):
    try:
        response = requests.post(url, data=data)
        response.encoding = "utf–8"
        print(response.text)
    except:
        print("\a发送失败\n请检查网络是否正常或页面是否存在")


def get(url, data):
    try:
        response = requests.get(url, params=data)
        response.encoding = "utf–8"
        print(response.text)
    except:
        print("\a发送失败\n请检查网络是否正常或页面是否存在")

# 提交表单


def upform(url):
    formname = []
    formvalue = []
    formdata = {}
    method = input("请选择方法:\n[1]post\n[2]get\n不作选择默认为post\n")
    n = int(input("请选择提交数量:"))
    for i in range(n):
        formname += [input("请输入第"+str(i+1)+"个变量名:")]
        formvalue += [input("请输入第"+str(i+1)+"个变量值:")]
    for i in range(n):
        formdata[formname[i]] = formvalue[i]
    if method in ["1", "post"]:
        post(url, formdata)
    elif method in ["2", "get"]:
        get(url, formdata)
    else:
        post(url, formdata)

# 后台文件扫描


def findadmin(url):
    def shaomiao(path):
        path = path.strip()
        try:
            txturl = url + path
            r = requests.get(txturl, headers)
            if r.status_code == requests.codes.ok:
                print(txturl)
        except:
            return 0

    kind = input(
        "请选择后台语言类型\n[0]全部\n[1]ASP\n[2]ASPX\n[3]DIR\n[4]JSP\n[5]MDB\n[6]PHP\n默认为全部\n")
    if kind in ["0", "全部"]:
        kind = 1
    elif kind in ["1", "ASP", "asp"]:
        kind = "ASP.txt"
    elif kind in ["2", "ASPX", "aspx"]:
        kind = "ASPX.txt"
    elif kind in ["3", "DIR", "dir"]:
        kind = "DID.txt"
    elif kind in ["4", "JSP", "jsp"]:
        kind = "JSP.txt"
    elif kind in ["5", "MDB", "mdb"]:
        kind = "MDB.txt"
    elif kind in ["6", "PHP", "php"]:
        kind = "PHP.txt"
    else:
        kind = 1

    if kind == 1:
        kind = ["ASP.txt", "ASPX.txt", "DIR.txt",
                "JSP.txt", "MDB.txt", "PHP.txt"]
        for ikind in kind:
            txtlist = path_dict.get_file(ikind)
            for i in txtlist:
                t1 = threading.Thread(target=shaomiao, args=(i,))
                t1.start()
    else:
        txtlist = path_dict.get_file(kind)
        for i in txtlist:
            # print("\r进度("+str(s+f)+"/"+str(num)+")",end="")
            t1 = threading.Thread(target=shaomiao, args=(i,))
            t1.start()


if __name__ == "__main__":
    getsrc(
        "https://miaobuao.github.io/"
    )
    ...
