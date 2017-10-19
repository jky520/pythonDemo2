__author__ = "@DT人"

names = ["jky","jack"]

data = {}

try:
    names[3]
except IndexError as e:
    print("列表下标越界异常", e)

try:
    data["name"]
except KeyError as e:
    print("没有这个key",e)

try:
    data["name"]
    names[3]
except (KeyError,IndexError) as e:
    print("没有这个key",e)
# except KeyError as e:
#     print("没有这个key",e)

try:
    names[4]
    data["data"]
    open("test.text")
except Exception as e:  #一次性处理所有的
    print("异常错误",e)

try:
    names[5]
    data["sex"]
    10/0
    open("test.text")
except IndexError as e:
    print("列表下标越界异常", e)
except KeyError as e:
    print("没有这个key",e)
except ArithmeticError as e:
    print("算术异常", e)
except Exception as e:
    print("未知错误", e)

else: # 当没有任何错误就走这里
    print("一切正常")
finally:
    print("不管有没有错都会执行")