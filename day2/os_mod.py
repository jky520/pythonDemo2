__author__ = "@DT人"

"""import os

#cmd_res = os.system("dir"); # 执行命令，不保存结果
cmd_res = os.popen("dir").read();

print("----->",cmd_res);
os.mkdir("new_dir");"""

msg = "我爱贵阳花果园";
print(msg.encode("utf-8").decode("utf-8"));  # String->bytes->string