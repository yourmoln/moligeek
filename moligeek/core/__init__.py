import os
info = {}
PATH = os.path.dirname(os.path.abspath(__file__))
with open(os.path.join(PATH, "../__version__.py"), 'r', encoding='utf8') as f:
    exec(f.read(), info)



__version__ = info['__version__']
__url__     = info['__url__']
__docs__ = rf"""=============================================
                 _ _                 _     
 _ __ ___   ___ | (_) __ _  ___  ___| | __
| '_ ` _ \ / _ \| | |/ _` |/ _ \/ _ \ |/ /
| | | | | | (_) | | | (_| |  __/  __/   < 
|_| |_| |_|\___/|_|_|\__, |\___|\___|_|\_\
                     |___/
v{__version__}
开源地址: {__url__}
本工具仅限于合法用途，交流Q群:564136017
============================================="""
