#1.有四个数字：1，2，3，4，能组成多少个互不相同且无重复数字的三位数？各是多少？

for i in range(1,5):
    for j in range(1,5):
        for k in range(1,5):
            if (i != k) and (i != j) and (j != k):
                print(i,j,k)

#2.企业发放的奖金根据利润提成。利润（l）低于或等于10万元时，奖金可提10%；利润高于10万元，低于20万元时，低于10万元的部分按10%提成，高于10万元的部分，可提成7.5%；20万到40万之间时，高于20万的部分，可提成5%；40万到60万之间时高于40万元的部分，可提成3%；60万到100万之间时，高于60万元的部分，可提成1.5%，高于100万元时，超过100万元的部分按1%提成，从键盘输入当月利润l，求应发放奖金总数？

i = int(input('输入你的利润值'))
arr = [1000000,600000,400000,200000,100000,0]
rat = [0.01,0.015,0.03,0.05,0.075,0.1]
result = 0
for idx in range(0,6):
    if i > arr[idx]:
        result += (i-arr[idx]) * rat[idx]
        i = arr[idx]
print (result)

#3.输入三个整数x，y，z，请把这三个数由小到大输出

my_list = []
for i in range(3):
    x = int(input('input :'))
    my_list.append(x)
my_list.sort()
my_list

#4.将一个列表的数据复制到另一个列表中

a = [1,2,3]
b = a[:]
print(b)

#5.暂停一秒输出并格式化当前的时间，使用time模块的sleep（）函数

import time
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
time.sleep(1)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))
time.sleep(2)
print(time.strftime('%Y-%m-%d %H:%M:%S', time.localtime(time.time())))

#6.打印出所有的“水仙花数”，所谓“水仙花数”是指一个三位数，其各位数字立方和等于该数本身。例如：153是一个“水仙花数”，因为153=1的三次方+5的三次方+3的三次方。

for x in range(1,10):
    for y in range(0,10):
        for z in range(0,10):
            s1 = x*100+y*10+z
            s2 = pow(x,3) + pow(y,3) + pow(z,3)
            if s1 == s2:
                print(s1)

#7.输入一行字符，分别统计出其中英文字母、空格、数字和其它字符的个数。

s = input("input:")
letters = 0
space = 0
digit = 0
others = 0
for c in s:
    if c.isalpha():
        letters += 1
    elif c.isspace():
        space += 1
    elif c.isdigit():
        digit += 1
    else:
        others += 1
print("char = %d, space = %d, digit = %d, others = %d" %(letters,space,digit,others))

#8.一球从100米高度自由落下，每次落地后反跳回原高度的一半；再落下，求它在第10次落地时，共经过多少米？第10次反弹多高？

h = 100 #总高度
time = 10  #次数
height = [] #反弹高度
for i in range(2, time+1):
    h /= 2
    height.append(h)
print(min(height)/2)
print(sum(height)*2+100)



