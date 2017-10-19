__author__ = "@DT人"

class JkyException(Exception): # 继承Exception类
    """自定义异常类JkyException"""

    def __init__(self,msg): # 构造函数
        self.message = msg # message表示类的属性

    def __str__(self):  # __str__相当于java的toString
        return self.message  # 返回实例的格式

try:
    raise JkyException("我的异常")  # raise 触发自己写的异常
except JkyException as e:
    print(e)

# try:
#     name = []
#     name[2]
# except JkyException as e:
#     print(e)