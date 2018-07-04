'''
'3位水仙花数计算 B


描述
"3位水仙花数"是指一个三位整数，其各位数字的3次方和等于该数本身。例如：ABC是一个"3位水仙花数"，则：A的3次方＋B的3次方＋C的3次方 = ABC。

请按照从小到大的顺序输出所有的3位水仙花数，请用"逗号"分隔输出结果。

注意：这是一个OJ题目，输出格式要严格一致。


输入
无

输出
示例：634, 412

(注意，这两个数字不是水仙花数)
'''
output = []
for d in range(100, 1000):
    x = d//100
    y = (d % 100)//10
    z = d % 10
    s = x**3 + y**3 + z**3
    if s == d:
        output.append(d)
#以下为输出格式调整
for i in range(len(output)):
    if i < len(output)-1:
        print(output[i], end=',')
    else:
        print(output[i])
