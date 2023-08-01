import base64,urllib

class todecode:
    def base64(self):
        try:
            return base64.b64decode(self.text.encode("utf-8")).decode("utf-8")
        except:
            return
    def base32(self):
        try:
            return base64.b32decode(self.text.encode("utf-8")).decode("utf-8")
        except:
            return
    def base16(self):
        try:
            return base64.b16decode(self.text.encode("utf-8")).decode("utf-8")
        except:
            return
    def url(self):
        try:
            return urllib.parse.unquote(self.text)
        except:
            return
    def unicode(self):
        try:
            return self.text.encode("utf-8").decode("unicode_escape")
        except:
            return
    def autodecode(self):
        return {"base64":self.base64(),"base32":self.base32(),"base16":self.base16(),"URL":self.url(),"unicode":self.unicode()}
    def __init__(self,text):
        self.text = text
if __name__ == "__main__":
    a = todecode("5L2g5aW9")
    print(a.autodecode())
    # a = derail("123456",5)