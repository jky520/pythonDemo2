__author__ = "@DT人"

a = [i+1 for i in range(10)]
print(a)

def fib(max):
    n, a, b = 0, 0, 1
    while n < max:
        #print(b)
        yield b
        a, b = b, a + b
        n += 1;
    return 'done' # retuen的作用是异常的时候打印信息

data = fib(10)

print(data.__next__())
print(data.__next__())
print(data.__next__())
print(data.__next__())
print(data.__next__())

print("=================")
# for i in data:
#     print(i)

f = fib(10)
while True:
    try:   # 异常处理
        x = fib(f)
        print("data:",x)
    except StopIteration as e:
        print("Generator return value:", e.value)
        break