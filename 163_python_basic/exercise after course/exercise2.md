数值计算小练习
描述
这是一个关于"数值计算"的小练习，覆盖整数、浮点数和复数运算，包含两部分内容：跟随练习 和 小测验。

在"跟随练习"环节，请使用IDLE编辑器的交互模式，逐一输入以下语句，观察并比较输出结果。

在"小测验"环节，请在本题目对应的"提交代码"页面按要求输入代码，"保存并提交评判"后查看结果。

跟随练习
 请使用IDLE编辑器的交互模式（含有>>>提示符），按顺序逐一输入以下语句（共15个）：

>>>a = 0xa + 0b1010 + 12.34
>>>b = int(11.99)
>>>print(a, b)
32.34 11
>>>a, b = b, a
>>>print(a, b)
11 32.34
>>>a = -a
>>>b = complex(b)
>>>print(a, b)
-11 (32.34+0j)
>>>a + b 
(21.340000000000003+0j)
>>>a + b == 21.34 + 0j
False
>>>a + b == 21.340000000000003
True
>>>round((a+b).real, 2) == 21.34
True
>>>hex(425)
'0x1a9'
>>>max(0x1a9, 425, 400)
425
>>>425/125
3.4
小测验
请将如下代码粘贴至"提交代码"页面，"保存并提交评判"后查看结果。注意，此时代码不是交互模式，而是文件模式。 

a = 123.456
b = 456.789
print(round(a+b, 3) == 580.245)

习题讲解
【代码分析】

a = 123.456
b = 456.789
print(round(a+b, 3) == 580.245)
数值运算中，浮点数运算后如果需要比较，一定要关注不确定尾数问题，即使用round()方法对输出结果小数部分进行约定，避免不确定尾数的干扰。

字符串操作小练习
描述
这是一个关于"字符串操作"的小练习，覆盖字符串索引、切片和基本操作方法，包含两部分内容：跟随练习 和 小测验。

在"跟随练习"环节，请使用IDLE编辑器的交互模式，逐一输入以下语句，观察并比较输出结果。

在"小测验"环节，请在本题目对应的"提交代码"页面按要求输入代码，"保存并提交评判"后查看结果。

跟随练习
 请使用IDLE编辑器的交互模式（含有>>>提示符），按顺序逐一输入以下语句（共35个）：

>>>"Python"
'Python'
>>>'python'
'python'
>>>"Python" == 'python'
False
>>>"Python" == 'Python'
True
>>>"Python"[0]
'P'
>>>"Python"[-1]
'n'
>>>s = "Python是一门好语言"
>>>print(s)
Python是一门好语言
>>>type(s)
<class 'str'>
>>>len(s)
12
>>>s[-2:-1]
'语'
>>>s[1:3]
'yt'
>>>s[:3]
'Pyt'
>>>s[-2:]
'语言'
>>>s[:]
'Python是一门好语言'
>>>s.split('是')
['Python', '一门好语言']
>>>t = "Python 是 一门 好语言"
>>>t.split()
['Python', '是', '一门', '好语言']
>>>s.replace("Python", "C")
'C是一门好语言'
>>>s
'Python是一门好语言'
>>>t
'Python 是 一门 好语言'
>>>t = s.replace("Python", "C")
>>>t
'C是一门好语言'
>>>s * 2
'Python是一门好语言Python是一门好语言'
>>>s
'Python是一门好语言'
>>>2 * s
'Python是一门好语言Python是一门好语言'
>>>s + t
'Python是一门好语言C是一门好语言'
>>>"Python" in s
True
>>>"C" in s
False
>>>"C" not in s
True
>>>"{}是一门好语言".format("Python")
'Python是一门好语言'
>>>"{}是一门好{}".format("Python","语言")
'Python是一门好语言'
>>>"{}".format(s)
'Python是一门好语言'
>>>"{:.2}".format(s)
'Py'
>>>"{:.6}".format(s)
'Python'
小测验
请将如下代码粘贴至"提交代码"页面，"保存并提交评判"后查看结果。注意，此时代码不是交互模式，而是文件模式。 

a = "Python语言"
b = "C"
print(a.replace("Python", b))

习题讲解
【代码分析】

a = "Python语言"
b = "C"
print(a.replace("Python", b))
字符串操作中，.replace(old, new)方法能够将字符串中old子串用new子串替换，替换后产生新的字符串，不改变a的内容。

分支循环操作小练习
描述
这是一个关于"分支循环操作"的小练习，覆盖分支、循环和异常的基本操作方法，包含两部分内容：跟随练习 和 小测验。

在"跟随练习"环节，请使用IDLE编辑器的交互模式，逐一输入以下语句，观察并比较输出结果。

在"小测验"环节，请在本题目对应的"提交代码"页面按要求输入代码，"保存并提交评判"后查看结果。

跟随练习
 请使用IDLE编辑器的交互模式（含有>>>提示符），按顺序逐一输入以下语句（共30个）：

>>>if 0:
      print("Hello")

>>>if 1:
      print("Hello")
Hello
>>>if "":
      print("Hello")

>>>if []:
      print("Hello")

>>>if {}:
      print("Hello")

>>>if "Not Empty":
      print("Hello")
Hello
>>>if [10, "101"]:
      print("Hello")
Hello
>>>if True:
      print("Hello")
Hello
>>>if False:
      print("Hello")

>>>if 0 == 1:
      print("Hello")

>>>a = 10
>>>if a > 10 or a < 10:
   print("a is not 10")
else:
   print("a is 10")

a is 10
>>>if a >10:
    print("a > 10")
elif a < 10:
    print("a < 10")
else: 
    print("a = 10")

a = 10
>>>range(10)
range(0, 10)
>>>list(range(10))
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>for i in range(10):
       print(i, end="")
0123456789
>>>for i in [0, 1, 2, 3, 4]:
       print(i, end="")
01234
>>>for i in range(1, 10, 2):
       print(i, end="")
13579
>>>list(range(1, 10, 2))
[1, 3, 5, 7, 9]
>>>for c in "Python语言":
       print(c)
P
y
t
h
o
n
语
言
>>>for c in "Python语言":
       print(c, end=",")
P,y,t,h,o,n,语,言,
>>>while a > 5:
      print(a)
      a = a - 1
10
9
8
7
6

>>>while False:
       print("Hello")

>>>while True:
	print("Hello")
	break
Hello
>>>a
5
>>>while a > 0:
     a = a - 1
     if a % 2 == 0:
        continue
     print(a)

3
1
>>>try:
       a = 10/0
except:
       print("error")

error
>>>try:
       a = open("no-exist")
except:
       print("error")

error
>>>try:
    if x:
        print("Hello")
except:
       print("error")

error
>>>try:
    anyerror
except:
       print("error")

error
小测验
请将如下代码粘贴至"提交代码"页面，"保存并提交评判"后查看结果。注意，此时代码不是交互模式，而是文件模式。 

a = 10
try:
   while True:
      print("{:.2f}".format(10/a))
      a = a - 1
except:
   print("infinity")

习题讲解
【代码分析】

a = 10
try:
   while True:
      print("{:.2f}".format(10/a))
      a = a - 1
except:
   print("infinity")
这个例子用到了try-except捕捉除数为0的结束情况，while True在编程中十分常用，需要在其中设定结束条件或异常条件。

这是一个利用异常处理结束while True无限循环的典型实例。

列表操作小练习
描述
这是一个关于"列表操作"的小练习，覆盖列表类型的定义及使用的基本操作方法，包含两部分内容：跟随练习 和 小测验。

在"跟随练习"环节，请使用IDLE编辑器的交互模式，逐一输入以下语句，观察并比较输出结果。

在"小测验"环节，请在本题目对应的"提交代码"页面按要求输入代码，"保存并提交评判"后查看结果。

跟随练习
 请使用IDLE编辑器的交互模式（含有>>>提示符），按顺序逐一输入以下语句（共20个）：

>>>[]
[]
>>>[1,2,"1","2"]
[1, 2, '1', '2']
>>>ls = [1,2,"1","2", [1, 2, 3, 4]]
>>>ls[0]
1
>>>ls[-1]
[1, 2, 3, 4]
>>>ls[-1][-1]
4
>>>ls[0:3]
[1, 2, '1']
>>>ls[-4: -1]
[2, '1', '2']
>>>ls*2
[1, 2, '1', '2', [1, 2, 3, 4], 1, 2, '1', '2', [1, 2, 3, 4]]
>>>ls
[1, 2, '1', '2', [1, 2, 3, 4]]
>>>ls.append(5)
>>>ls
[1, 2, '1', '2', [1, 2, 3, 4], 5]
>>>ls.remove(ls[-1])
>>>ls
[1, 2, '1', '2', [1, 2, 3, 4]]
>>>len(ls)
5
>>>del ls[3]
>>>ls
[1, 2, '1', [1, 2, 3, 4]]
>>>ls[::-1]
[[1, 2, 3, 4], '1', 2, 1]
>>>ls.clear()
>>>ls
[]
小测验
请将如下代码粘贴至"提交代码"页面，"保存并提交评判"后查看结果。注意，此时代码不是交互模式，而是文件模式。 

ls = list(range(1, 11))
sum = 0
for i in ls:
     sum += i
print(sum)

习题讲解
【代码分析】

ls = list(range(1, 11))
sum = 0
for i in ls:
     sum += i
print(sum)
list()函数能把range()函数产生的类型转换为列表类型，for .. in..对列表元素逐一遍历并求和。

该程序比较简单，需要注意：在Python3中，range()产生特定的range类型，并不是列表类型，但可以通过list()函数进行转换。

多输入均值
描述
用户在一行内输入多个数值，采用空格分隔，求这些输入数值的均值，保留小数点后一位。

不考虑异常输入。

输入格式
输入一行多个数值，采用空格分隔。

输出格式
一个数值

输入输出示例
 	输入	输出
示例 1	
1 1 2 3 5 8 13 21 34
9.8

txt = input()
ls = txt.split()
sum = 0
for num in ls:
    sum += eval(num)
print('{:.1f}'.format(sum/len(ls)))

习题讲解
【参考代码】

txt = input()
ls = txt.split()
sum = 0
for item in ls:
    sum += eval(item)
print("{:.1f}".format(sum/len(ls)))
input()获得的输入是字符串，可以利用.split()方法分隔各元素，行程列表ls。进一步，采用eval()将每个元素变成数值类型，进一步求平均值。

多输入数字求和
描述
用户输入一批数字，每个数字一行，输入一个数字之后回车在下一行输入下一个数字，最后以空回车为结束（即空输入）。

计算这批数字的和。 

输入格式
每行一个数字，可以是多行。

输出格式
一个数字

输入输出示例
 

 	输入	输出
示例 1	
999
1
1000

sum = 0
txt = input()
while txt !="":
    sum += eval(txt)
    txt = input()
print(sum)

习题讲解
【参考答案】

sum = 0
txt = input()
while txt != "":
    sum += eval(txt)
    txt = input()
print(sum)
这个题目重点考察对于不确定多输入的处理，采用while和input()组合实现，代码不难，请参考一下。

英文单词个数统计
描述
给出一个字符串s，内容在"编程模板"中，请统计并打印字符串s中出现单词的个数。

输入格式
给定的字符串

输出格式
一个整数

输入输出示例
只是格式示例，输出不是正确答案

 	输入	输出
示例 1	 	
10

s = '''
"Collusion is very real with Russia," Trump quoted conservative commentator Dan Bongino as saying on Trump's favorite Fox News morning show, "but only with Hillary and the Democrats, and we should demand a full investigation."
'''
s = s.replace('"', ' ')
s = s.replace(',', ' ')
s = s.replace('.', ' ')
ls = s.split()
print(len(ls))

习题讲解
【参考代码】

s = '''
"Collusion is very real with Russia," Trump quoted conservative commentator Dan Bongino as saying on Trump's favorite Fox News morning show, "but only with Hillary and the Democrats, and we should demand a full investigation."
'''
s = s.replace('"', ' ')
s = s.replace(',', ' ')
s = s.replace('.', ' ')
ls = s.split()
print(len(ls))
统计单词个数，一个重要环节是去掉标点符号。这里采用将标点符号替换为空格的方式。使用字符串s.replace(old, new)方法，能够将字符串中old子串替换为new子串。

也可以逐一遍历字符串进行处理。

传感器日志输出
描述
本题目附件提供了一个传感器日志文件，为文本类型，共1千行，每行包含了日期、时间和4种传感器读数值。

在Python123中读取文件请假设题目对应文件在当前目录下，文件打开函数参考如下：

f=open("sensor-data-1k.txt", "r")
编写程序，输出该文件中第N*100行内容，其中N为整数，即输出第100行、第200行等内容，各行内容之间没有空行。

输入格式
附件 senor-data-1k.txt文件

输出格式
字符输出

输入输出示例
仅以输出第100行为例（实际上应该输出共10行）

 	输入	输出
示例 1	无	
2018-02-28 03:28:47.036129 18.4008 39.1443 43.24 2.68742
 

附件
序号
名称 程序内使用说明
1
sensor-data-1k.txt

#2018-02-28 01:03:16.33393 19.3024 38.4629 45.08 2.68742
f = open("sensor-data-1k.txt", "r")
count = 0
for line in f:
    count += 1 
    if count % 100 ==0:
        print(line, end="")
f.close()

习题讲解
【参考代码】

f = open("sensor-data-1k.txt", "r")
count = 0
for line in f:
    count += 1 
    if count % 100 ==0:
        print(line, end="")
f.close()
for line in f: 语句可以遍历文件中的每一行，但要注意，此时没有对行数的统计，需要辅助变量count计数。

由于原文每行最后有一个换行，print()语句又增加了换行，所以，需要使用print(line, end="")去掉print()语句最后的换行，进而输出各行之间没有空行。

传感器日志光照统计
描述
本题目附件提供了一个传感器日志文件，为文本类型，共1千行，每行包含了日期、时间和4种传感器读数值。

其中，4种传感器读数值分别是：温度、湿度、光照和电压。

在Python123中读取文件请假设题目对应文件在当前目录下，文件打开函数参考如下：

f=open("sensor-data-1k.txt", "r")
编写程序，统计日志反应的光照平均值，保留小数点后2位。

输入格式
附件 senor-data-1k.txt文件

输出格式
数值

输入输出示例
结果仅表示格式，不是正确答案。

 	输入	输出
示例 1	无	
43.24
 

附件
序号
名称 程序内使用说明
1
sensor-data-1k.txt

f = open("sensor-data-1k.txt", "r")
sum, cnt = 0, 0
for line in f:
    ls = line.split()
    cnt += 1
    sum += eval(ls[4])
print("{:.2f}".format(sum / cnt))
f.close

习题讲解
【参考代码】

f = open("sensor-data-1k.txt", "r")
sum, cnt = 0, 0
for line in f:
    ls = line.split()
    cnt += 1
    sum += eval(ls[4])
print("{:.2f}".format(sum/cnt))
f.close()
line.split()根据空格将每行信息分割成多个元素，保存在列表中，其中序号4为光照值。

可以观察一下光照值在日志中的内容，可以发现，与温度湿度不同，这个值变化非常大。