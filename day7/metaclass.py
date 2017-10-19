__author__ = "@DT人"

class MyType(type):
    def __init__(self, what, bases=None, dict=None):
        print("--MyType init---")
        super(MyType, self).__init__(what, bases, dict)

    def __call__(self, *args, **kwargs):
        print("--MyType call----")
        obj = self.__new__(self, *args, **kwargs)
        self.__init__(obj, *args, **kwargs)


class Foo(object):
    __metaclass__ = MyType  # 与父类关联

    def __init__(self,name):
        self.name = name;
        print("Foo ---init__")

    def __new__(cls, *args, **kwargs): # 实例化对象的，在这个函数调用__init__初始化的
        print("Foo --new__")
        return object.__new__(cls) # 集成父类的__new__方法

f = Foo("jky")

print(f.name)