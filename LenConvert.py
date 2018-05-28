LenStr = input("请输入带有符号的长度值：")
if LenStr[-1] in ['M','m']:
    I = (eval(LenStr[0:-1]))*39.37
    print("转换后的长度是{:.3f}in".format(I))
elif LenStr[-2:] in ['in','IN','In']:
    L = eval(LenStr[0:-2])/39.37
    print("转换后的长度是{:.3f}m".format(L))
else:
    print("输入格式错误")
