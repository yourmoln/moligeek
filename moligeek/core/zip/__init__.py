import zipfile,time,threading,meo

def zipkey(file):
    def zipopen(file,password):
        try:
            #print(password)
            password = str(password)
            file.extractall(path='./', pwd=password.encode('utf-8'))
            print("破解成功，压缩包密码为 %s ,用时 %s"%(password,time.time-start_time))
        except:
            pass
    start_time = time.time()
    zfile = zipfile.ZipFile(file)
    for number in range(999999999):
        tzip = threading.Thread(target=zipopen, args=(zfile, number))
        tzip.start()
        tzip.join

if __name__ == "__main__":
    zipkey(r"C:\Users\Administrator\Desktop\1231.zip")
    ...

