import zipfile
import time
import asyncio
from tqdm.asyncio import tqdm
from itertools import permutations
import multiprocessing
import itertools

#PWD_SEED = b"1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+-=[{}]\|;:,<.>/?'\" "
PWD_SEED = ""
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
    
def guess_number_pwd(file):
    start_time = time.time()
    zfile = zipfile.ZipFile(file)
    print("开始爆破(纯数字)")
    for number in tqdm(range(999999999)):
        pwd = str(number).encode("utf8")
        if try_open_zip(zfile, pwd):
            print("破解成功，压缩包密码为 %s ,用时 %s s"%(str(pwd), int(time.time()-start_time)))
            return pwd
            
def key_permution(seed, size):
    for k in permutations(seed, size):
        yield bytes(k)

def key_generator(start=None, end=None, seed=PWD_SEED):
    n_size = 0 if start is None else int(start)
    if end is None:
        while True:
            n_size += 1
            for k in key_permution(PWD_SEED, n_size):
                yield k, n_size
    else:
        end = int(end)
        while True:
            n_size += 1
            if n_size <= end:
                for k in key_permution(PWD_SEED, n_size):
                    yield k, n_size

async def guess_async(path, min_length=None, max_length=None):
    zfile = zipfile.ZipFile(path)

    async def block(pwd):
        if try_open_zip(zfile, pwd):
            return pwd
        return False
    
    with tqdm(key_generator(min_length, max_length)) as bar:
        async for pwd, n_size in bar:
            if await block(pwd):
                return pwd
    return None

def guess_pwd_normal(path, min_length=None, max_length=None):
    start_time = time.time()
    loop = asyncio.get_event_loop()
    future = asyncio.ensure_future(guess_async(path, min_length, max_length))
    loop.run_until_complete(future)
    pwd = future.result()
    if pwd:
        print("破解成功，压缩包密码为 %s ,用时 %s s"%(pwd.decode("utf8"), time.time() - start_time))
    else:
        print("破解失败！")
    return pwd

def __block(file, pwds):
    zfile = zipfile.ZipFile(file)
    for pwd, _ in pwds:
        if try_open_zip(zfile, pwd):
            return pwd
    return False


def guess_in_multiprocess(path, min_length=None, max_length=None, n_processes=8, slice_size=500):
    pool = multiprocessing.Pool(n_processes)
    it = key_generator(min_length, max_length)
    manager = multiprocessing.Manager()
    info = manager.dict()
    info['key'] = None
    def cb(re):
        if re:
            info['key'] = re
            pool.terminate()
    while True:
        for _ in range(n_processes):
            try:
                pwds = itertools.islice(it, 0, slice_size)
                pool.apply_async(__block, (path, list(pwds)), callback=cb)
            except Exception as e:
                if e.args[0] == 'Pool not running':
                    return info['key']
                else:
                    raise e

class ZipPasswordGuesser:

    def __init__(self, path, seed=PWD_SEED) -> None:
        self.seed = seed
        self.path = path

    def guess_number(self):
        return guess_number_pwd(self.path)
    
    async def guess_async(self, min_length=None, max_length=None):
        return await guess_async(self.path, min_length, max_length)
    
    def guess_normal(self, min_length=None, max_length=None):
        return guess_pwd_normal(self.path, min_length, max_length)
    
    def guess_mp(self, min_length=None, max_length=None, n_processes=8, slice_size=500):
        return guess_in_multiprocess(self.path, min_length, max_length, n_processes, slice_size)

def zipkey(path,mode):
    global PWD_SEED
    if mode in ["number",0]:
        PWD_SEED = b"1234567890"
    elif mode in ["letter + number",1]:
        PWD_SEED = b"1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"
    elif mode in ["letter + number + symbol",2]:
        PWD_SEED = b"1234567890qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM!@#$%^&*()_+-=[{}]\|;:,<.>/?'\" "
    st = time.time()
    zp = ZipPasswordGuesser(path)
    k = zp.guess_mp(n_processes=16, slice_size=1000)
    #k = zp.guess_normal()
    ed = time.time()
    print(f"密码为{k.decode('utf8')},总计用时{int((ed - st)*10)/10}s")
if __name__ == "__main__":
    # zipkey_plus(r"C:\Users\yourm\Desktop\1\flag.zip")
    # guess_pwd("./test/flag.zip")
    # st = time.time()
    # zp = ZipPasswordGuesser("./test/flag.zip")
    # k = zp.guess_mp(n_processes=16, slice_size=1000)
    # k = zp.guess_normal()
    # print(k)
    # ed = time.time()
    # print(ed - st)
    zipkey(r"C:\Users\yourm\Desktop\1\flag.zip",1)
    ...
