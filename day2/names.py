__author__ = "@DT人"

import copy

# 数组的使用
names = ["张三","李四","王五"];
print(names[0]);
print(names[1:4]) # 取范围

person = ['name',['a',100]];

p1 = copy.copy(person); # 1、浅copy
p2 = person[:]; # 2、浅copy
p3 = list(person) # 3、浅copy
print(p2)