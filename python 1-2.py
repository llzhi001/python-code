#print('祖国，您好!')
#print('我来了，学好Python。')

HeatStr = input("请输入带有符号的热量值：")
if HeatStr[-1] in ['J', 'j']:
    c = eval(HeatStr[0:-1]) / 4.186
    print("转换后的热量是{:.3f}cal".format(c))
elif HeatStr[-3:] in ['cal', 'Cal','CAL']:
    joule = eval(HeatStr[0:-3]) * 4.186
    print("转换后的热量是{:.3f}J".format(joule))
else:
    print("输入格式错误")
