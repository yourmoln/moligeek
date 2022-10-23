import base64,urllib

class todecode:
    def base64(self,text):
        try:
            return base64.b64decode(text.encode("utf-8")).decode("utf-8")
        except:
            return
    def url(self,text):
        try:
            return urllib.parse.unquote(text)
        except:
            return
    def unicode(self,text):
        try:
            return text.encode("utf-8").decode("unicode_escape")
        except:
            return
    def __init__(self,text):
        print("base64:",self.base64(text))
        print("URL:",self.url(text))
        print("unicode:",self.unicode(text))

class derail:
    def decode(self,text,lengh):
        text = list(text)
        l = len(text)
        tmp = ['']*l
        add = l%lengh
        if add > 0:
            for i in range(add):
                text.append("")
                tmp.append("")
            print(text)
        gn = int(len(text)/lengh)
        for i in range(lengh):
            for j in range(gn):
                if i*gn+j < l and i+lengh*j < l:
                    tmp[i+lengh*j]=text[i*gn+j]
                elif i+lengh*j > l-1 and i*gn+j < l:
                    print(text[i*gn+j])
                    tmp[(i+lengh*j - l - 1)*lengh - 1] = text[i*gn+j]
        output = ''.join(tmp)
        return output
    def __init__(self,text,lengh):
        print(self.decode(text,lengh))
if __name__ == "__main__":
    #a = todecode("5L2g5aW9")
    a = derail("123456",5)