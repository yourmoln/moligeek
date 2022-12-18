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
    def decode_rail_fence_cipher(self,cipher: str, num_rails: int) -> str:
        # 将密文分成 num_rails 个字符一组
        groups = [cipher[i::num_rails] for i in range(num_rails)]
        # 将每组的字符串连接起来，形成明文
        return ''.join([''.join(group) for group in groups])
    def __init__(self,text,lengh):
        print(self.decode_rail_fence_cipher(text,lengh))

if __name__ == "__main__":
    #a = todecode("5L2g5aW9")
    a = derail("123456",5)