__author__ = "@DT人"

def bulk(self):
    """类外定义的嚎叫函数"""
    print("%s 在狂叫...." % self.name)

class Dog(object):

    def __init__(self, name):
        self.name = name;

    def eat(self, food):
        print("%s is eatting %s" % (self.name, food))


d = Dog("泰迪")

choice = input(">>:").strip()

if hasattr(d,choice): # hasattr判断对象d中是否有某个choice属性或方法
    # func = getattr(d, choice) # getattr获得对象d中的choice属性或方法
    # func("肉")
    # 上面是处理方法属性的
    # attr = getattr(d, choice)
    # setattr(d, choice, "狼犬") # 重新给属性赋值
    delattr(d, choice) # 删除d对象的choice属性或方法
else:
    # setattr(d, choice, bulk) # 给对象装配d添加bulk属性
    # d.talk(d)
    setattr(d, choice, None);
    print(getattr(d, choice))

print(d.name)
