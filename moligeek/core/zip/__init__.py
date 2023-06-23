import zipfile
import time
import threading
from tqdm import tqdm
from itertools import permutations

PERMUTE = b"1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+-=[{}]\|;:,<.>/?'\" "

def try_open_zip(file, pwd):
    try:
        if isinstance(pwd, str):
            pwd = pwd.encode('utf8')
        mem = file.namelist()[0]
        with file.open(mem, pwd=pwd) as f:
            if f.seek(1):
                return True
    except:
        return False
    
def zipkey(file):
    start_time = time.time()
    zfile = zipfile.ZipFile(file)
    print("开始爆破(纯数字)")
    for number in tqdm(range(999999999)):
        if try_open_zip(zfile,number) == 1:
            print("破解成功，压缩包密码为 %s ,用时 %s s"%(number,int(time.time()-start_time)))
            break


def key_generator(start=None, end=None):
    n_size = 0 if start is None else int(start)
    if end is None:
        while True:
            n_size += 1
            for k in permutations(PERMUTE, n_size):
                yield bytes(k)
    else:
        end = int(end)
        while True:
            n_size += 1
            if n_size <= end:
                for k in permutations(PERMUTE, n_size):
                    yield bytes(k)

def zipkey_plus(file, min_length=None, max_length=None):
    start_time = time.time()
    zfile = zipfile.ZipFile(file)
    break_out_flag = False
    with tqdm(key_generator(min_length, max_length)) as t:
        for pwd in t:
            if try_open_zip(zfile, pwd):
                break_out_flag = True
                break
    if break_out_flag:
        print("破解成功，压缩包密码为 %s ,用时 %s s"%(pwd.decode("utf8"), int(time.time() - start_time)))
    else:
        print("破解失败！")

if __name__ == "__main__":
    # zipkey_plus(r"C:\Users\yourm\Desktop\1\flag.zip")
    zipkey_plus("./test/flag.zip")
    ...
