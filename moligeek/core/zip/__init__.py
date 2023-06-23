import zipfile,time,threading,meo
from tqdm import tqdm
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

if __name__ == "__main__":
    zipkey(r"C:\Users\yourm\Desktop\1\flag.zip")
    ...

