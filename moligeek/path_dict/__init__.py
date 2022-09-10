import sys
import os

__dir__ = os.path.split(os.path.realpath(__file__))[0]

def get_file_path(name):
    return os.path.join(__dir__, name)

def get_file(name, encoding='gbk'):
    fpath = get_file_path(name)
    with open(fpath, 'r', encoding=encoding) as f:
        return f.readlines()
