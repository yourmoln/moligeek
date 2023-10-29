import math

def decrypt(cipher:str, key:int) -> str:
    """`栅栏密码`的解密函数. 与`千千秀字`的结果一致."""
    assert type(key) is int

    cipsize = len(cipher)
    gsize = math.ceil(cipsize / key)
    psize = gsize * key - cipsize
    common_count = key - psize        # 正常解码的行数

    res = ''
    for i in range(gsize):
        j = i
        while j < cipsize and (i < common_count or j < common_count * gsize):
            res += cipher[j]
            j += gsize if j < common_count * gsize else gsize - 1
    return res

def encrypt(plain:str, key:int) -> str:
    """`栅栏密码`的加密函数. """
    assert type(key) is int

    plain_size = len(plain)
    gcount = math.ceil(plain_size / key)
    common_size = key * (1 - gcount) + plain_size

    res = ''
    for i in range(key):
        j = i
        while j < plain_size and (i < common_size or j < key * (gcount - 1)):
            res += plain[j]
            j += key
    return res

if __name__ == "__main__":
    plain = "123456789abcdef"
    key = 4
    _enc = encrypt(plain, key)
    _dec = decrypt(_enc, key)
    print("_enc:", _enc)
    print("_dec:", _dec)
    