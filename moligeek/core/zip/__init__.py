import zipfile,time,threading,meo
from tqdm import tqdm
from itertools import permutations
def zipkey(file):
    def zipopen(file,password):
        try:
            password = str(password)
            file.extractall(path='./zipout/', pwd=password.encode('utf-8'))
            return 1
        except:
            return 0
    start_time = time.time()
    zfile = zipfile.ZipFile(file)
    print("开始爆破(纯数字)")
    for number in tqdm(range(999999999)):
        if zipopen(zfile,number) == 1:
            print("破解成功，压缩包密码为 %s ,用时 %s s"%(number,int(time.time()-start_time)))
            break

def zipkey_plus(file):
    def zipopen(file,password):
        try:
            password = str(password)
            file.extractall(path='./zipout/', pwd=password.encode('utf-8'))
            return 1
        except:
            return 0
    start_time = time.time()
    zfile = zipfile.ZipFile(file)
    break_out_flag = False
    dict = [chr(d) for d in range(65,91)]+[chr(x) for x in range(97,123)]+[str(num) for num in range(10)]
    for i in range(100):
        print(f"正在破解{i+1}位数密码")
        password_list = list(permutations(dict,i+1))
        for password in tqdm(password_list):
            password = "".join(password)
            if zipopen(zfile,password) == 1:
                print("破解成功，压缩包密码为 %s ,用时 %s s"%(password,int(time.time()-start_time)))
                break_out_flag = True
                break
        if break_out_flag:
            break


if __name__ == "__main__":
    zipkey_plus(r"C:\Users\yourm\Desktop\1\flag.zip")
    ...

