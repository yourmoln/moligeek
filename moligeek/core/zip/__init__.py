import zipfile
import time
import asyncio
from tqdm.asyncio import tqdm
from itertools import permutations

PERMUTE = b"1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+-=[{}]\|;:,<.>/?'\" "

def try_open_zip(file, pwd):
    assert isinstance(file, zipfile.ZipFile)
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
                yield bytes(k), n_size
    else:
        end = int(end)
        while True:
            n_size += 1
            if n_size <= end:
                for k in permutations(PERMUTE, n_size):
                    yield bytes(k), n_size

def zipkey_plus(file, min_length=None, max_length=None):
    start_time = time.time()
    zfile = zipfile.ZipFile(file)

    async def block(pwd):
        if try_open_zip(zfile, pwd):
            return pwd
        return False

    async def generator():
        with tqdm(key_generator(min_length, max_length)) as bar:
            # queue = []
            # max_q_size, q_size = 10000, 0
            # last_size = -1
            async for pwd, n_size in bar:
                if await block(pwd):
                    return pwd
                # if q_size >= max_q_size:
                #     res = await asyncio.gather(*queue)
                #     for p in set(res):
                #         if p:
                #             return p
                #     queue = []
                #     q_size = 0
                # queue.append(block(pwd))
                # q_size += 1
        return None
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(generator())
    loop.run_until_complete(future)
    pwd = future.result()
    if pwd:
        print("破解成功，压缩包密码为 %s ,用时 %s s"%(pwd.decode("utf8"), time.time() - start_time))
    else:
        print("破解失败！")
    return pwd

if __name__ == "__main__":
    # zipkey_plus(r"C:\Users\yourm\Desktop\1\flag.zip")
    zipkey_plus("./test/flag.zip")
    ...
