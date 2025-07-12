import re
import meo
import requests
import threading
import sys
import os
from tqdm import tqdm
from concurrent.futures import ThreadPoolExecutor, as_completed

script_path = os.path.split(os.path.realpath(__file__))[0]
sys.path.append(os.path.join(script_path, "../../"))
import path_dict

#仿站
from .imitate import Imitate

HOST_PATTERN = r".+://(.+)"
headers = {
    "User-Agent": meo.net.UserAgent.FIREFOX
}


def getsrc(url:str, output=None, headers=headers) -> str:
    """获取网站源码并保存到`./output/`"""
    host_match = re.match(HOST_PATTERN, url)
    host = host_match.group(1)
    try:
        response = requests.get(url, headers)
        response.encoding = "utf-8"
        fname = host.replace("/", "_")
        if output is None:
            output = f"./output/{fname}"
        meo.to_file(output, response.text)
        return output
    except:
        return None


def post(url:str, data:dict) -> str:
    """以`post`的方式提交表单"""
    try:
        response = requests.post(url, data=data)
        response.encoding = "utf-8"
        return response.text
    except:
        return None


def get(url:str, data:dict) -> str:
    """以`get`的方式提交表单"""
    try:
        response = requests.get(url, params=data)
        response.encoding = "utf-8"
        return response.text
    except:
        return None

def upform(url:str,method:str = 'get',formdata:dict = None) -> str:
    """提交表单"""
    if method in ["1", "post"]:
        return post(url, formdata)
    elif method in ["2", "get"]:
        return get(url, formdata)
    else:
        return None

def findadmin(url,kind = 1):
    """后台文件扫描"""
    up_list = []
    def scan(path):
        path = path.strip()
        try:
            txturl = url + path
            r = requests.get(txturl, headers)
            if r.status_code == requests.codes.ok:
                up_list.append(txturl)
        except:
            return 0

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
    # Create a list of threads
    if kind == 1:
        kind = ["ASP.txt", "ASPX.txt", "DIR.txt",
                "JSP.txt", "MDB.txt", "PHP.txt"]
        with ThreadPoolExecutor() as executor:
            futures = []
            for ikind in kind:
                txtlist = path_dict.get_file(ikind)
                for i in tqdm(txtlist):
                    futures.append(executor.submit(scan, i))
            for future in as_completed(futures):
                pass
    else:
        txtlist = path_dict.get_file(kind)
        with ThreadPoolExecutor() as executor:
            futures = []
            for i in tqdm(txtlist):
                futures.append(executor.submit(scan, i))
            for future in as_completed(futures):
                pass
    return up_list
if __name__ == "__main__":
    getsrc(
        "https://miaobuao.github.io/"
    )
