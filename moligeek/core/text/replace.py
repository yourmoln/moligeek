# 检测并去除引号
def remove_quotes(string):
    if len(string) >= 2 and string[0] == string[-1] and (string[0] == '"' or string[0] == "'"):
        return string[1:-1]
    return string


def reKey(file:str, key:str, tokey:str) -> None:
    """替换关键词"""
    file = remove_quotes(file)
    with open(file,"r") as f:
        content = f.read() #读行
    content = content.replace(key, tokey)
    with open(file,"w") as f:
        f.write(content)
if __name__ == "__main__":
    reKey(r"C:\Users\yourm\Desktop\1\text.txt","test","_t_")