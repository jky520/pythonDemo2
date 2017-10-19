__author__ = "@DT人"

# 客户端
import socket

client = socket.socket() # 声明socket类型，同时生成socket连接对象
client.connect(('localhost',6969))

client.send("大家好".encode("utf-8")) # 在字符串前加上b表示将字符串转换成byte类型
data = client.recv(1024)
print("recv:",data)

client.close()



