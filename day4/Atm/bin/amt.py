__author__ = "@DT人"

import os
import sys

BASE_DIR = os.path.dirname(os.path.dirname( os.path.abspath(__file__) )) # 获得项目的根目录

sys.path.append(BASE_DIR) # 把根目录加入到环境变量中去

# import conf, core;

from conf import settings # 导入conf目录下的settings文件
from core import main # 导入core目录下的main文件怎么回事

main.login()