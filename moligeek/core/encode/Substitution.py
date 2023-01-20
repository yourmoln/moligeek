from Technology import password as pd
import json
import pathlib

def ReadDict(String:str):
    if pathlib.Path(String).is_file():
        try:
            with open(String, "r", encoding="utf-8") as file:
                _dict = file.read
        except:
            return None
    else:
        _dict = String
    try:
        return json.loads(_dict)
    except:
        return None

def Asked(password):
    _dict = ReadDict(input("请输入加密字典的路径或直接输入字典\n"))
    if _dict is None:
        print("字典读取出错，请重新输入")
        return False
    else:
        _ = input("请输入解密的模式:\n[1]严格\n[2]忽略\n[3]保留\n")
        mode = 0 if _ in ["1", "严格"] else 1 if _ in ["2", "忽略"] else 2 if _ in ["3", "保留"] else None
        if mode is None:
            print("模式选择错误，请重新")
            return False
        try:
            _Text = pd.Decrypt().Substitution(password, _dict, pd.Password().Mode[mode])
        except:
            return False