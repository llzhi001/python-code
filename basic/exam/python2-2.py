# 通过用户输入数字计算阶乘

# 获取用户输入的数字
a = input()
flag = 0
s = 0
if a.isdigit():
    b = eval(a)
    if b > 0:
        flag = 1
        temp = 1
        for i in range(b):
            s = s + (i+1) * temp
            temp = (i+1) * temp
if flag == 0:
    print("输入有误，请输入正整数")
else:
    print(s)
