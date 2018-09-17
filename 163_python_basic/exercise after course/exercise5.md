常用标准库之time/random小练习
描述
这是一个关于"常用标准库之time/random"的小练习，覆盖time库和random库的基本操作，包含两部分内容：跟随练习 和 小测验。

在"跟随练习"环节，请使用IDLE编辑器的交互模式，逐一输入以下语句，观察并比较输出结果。

在"小测验"环节，请在本题目对应的"提交代码"页面按要求输入代码，"保存并提交评判"后查看结果。

跟随练习
 请使用IDLE编辑器的交互模式（含有>>>提示符），按顺序逐一输入以下语句（共50个）：

>>>import time
>>>s = time.time()
>>>s
1534551957.9329424
>>>time.ctime(s)
'Sat Aug 18 08:25:57 2018'
>>>time.gmtime(s)
time.struct_time(tm_year=2018, tm_mon=8, tm_mday=18, tm_hour=0, tm_min=25, tm_sec=57, tm_wday=5, tm_yday=230, tm_isdst=0)
>>>time.localtime(s)
time.struct_time(tm_year=2018, tm_mon=8, tm_mday=18, tm_hour=8, tm_min=25, tm_sec=57, tm_wday=5, tm_yday=230, tm_isdst=0)
>>>t = time.gmtime()
>>>t
time.struct_time(tm_year=2018, tm_mon=8, tm_mday=18, tm_hour=0, tm_min=25, tm_sec=57, tm_wday=5, tm_yday=230, tm_isdst=0)
>>>time.mktime(t)
1534523157.0
>>>time.asctime(t)
'Sat Aug 18 00:25:57 2018'
>>>time.strftime("%Y-%m-%d", t)
'2018-08-18'
>>>time.strftime("%H:%M:%S", t)
'00:25:57'
>>>time.strftime("%b %a %p", t)
'Aug Sat AM'
>>>t1 = time.strptime("2018-10-10", "%Y-%m-%d")
>>>t1
time.struct_time(tm_year=2018, tm_mon=10, tm_mday=10, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=2, tm_yday=283, tm_isdst=-1)
>>>t2 = time.strptime("12:01:01","%H:%M:%S")
>>>t2
time.struct_time(tm_year=1900, tm_mon=1, tm_mday=1, tm_hour=12, tm_min=1, tm_sec=1, tm_wday=0, tm_yday=1, tm_isdst=-1)
>>>t3 = time.strptime("2017=09=10","%Y=%m=%d")
>>>t3
time.struct_time(tm_year=2017, tm_mon=9, tm_mday=10, tm_hour=0, tm_min=0, tm_sec=0, tm_wday=6, tm_yday=253, tm_isdst=-1)
>>>t3 - t1
Traceback (most recent call last):
  File "<pyshell#39>", line 1, in <module>
    t3 - t1
TypeError: unsupported operand type(s) for -: 'time.struct_time' and 'time.struct_time'
>>>time.mktime(t1) - time.mktime(t3)
34128000.0
>>>start = time.perf_counter()
>>>start
5.68888727071651e-07
>>>time.sleep(3)
>>>end = time.perf_counter()
>>>end-start
19.309388143107373

>>>from random import *
>>>random()
0.7142054643506315
>>>random()
0.9222291496048237
>>>seed(1024)
>>>random()
0.7970515714521261
>>>randint(1, 10)
8
>>>randrange(1, 10, 2)
7
>>>seed(1024)
>>>random()
0.7970515714521261
>>>randint(1, 10)
8
>>>randrange(1, 10, 2)
7
>>>ls= list(range(10))
>>>ls
[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
>>>shuffle(ls)
>>>ls
[6, 0, 7, 9, 2, 4, 3, 1, 8, 5]
>>>sample(ls, 3)
[7, 3, 0]
>>>choice(ls)
3
>>>getrandbits(10)
138
>>>getrandbits(1024)
3280201695238716936239020684624047456...(略)
>>>uniform(10,1000)
168.03388435941432
>>>uniform(10,1000)
395.2623313887394
>>>betavariate(10, 100)
0.06945246213487724
>>>betavariate(10, 100)
0.11142309099887106
>>>lognormvariate(10, 100)		   
5.364956236648193e+113
小测验
请将如下代码粘贴至"提交代码"页面，"保存并提交评判"后查看结果。注意，此时代码不是交互模式，而是文件模式。 

import random
ls = list(range(100))
random.seed(max(ls))
lt = random.sample(ls, 30)
for i in range(len(lt)):
    lt[i] = str(lt[i])
print(",".join(lt))

习题讲解
【代码分析】

import random
ls = list(range(100))
random.seed(max(ls))
lt = random.sample(ls, 30)
for i in range(len(lt)):
    lt[i] = str(lt[i])
print(",".join(lt))
此代码训练了random库的基本使用，种子确定，则程序每次运行结果一致，产生的随机数是伪随机数序列。

常用标准库之re小练习
描述
这是一个关于"常用标准库之re"的小练习，覆盖re库的基本操作，包含两部分内容：跟随练习 和 小测验。

在"跟随练习"环节，请使用IDLE编辑器的交互模式，逐一输入以下语句，观察并比较输出结果。

在"小测验"环节，请在本题目对应的"提交代码"页面按要求输入代码，"保存并提交评判"后查看结果。

跟随练习
 请使用IDLE编辑器的交互模式（含有>>>提示符），按顺序逐一输入以下语句（共30个）：

>>>import re
>>>match = re.search(r"[0-9]*[1-9][0-9]*","abcd1234")
>>>match.group(0) if match else "不匹配"
'1234'
>>>type(match)		   
<class '_sre.SRE_Match'>
>>>match.string		   
'abcd1234'
>>>match.re	   
re.compile('[0-9]*[1-9][0-9]*')
>>>match.pos		   
0
>>>match.endpos		   
8
>>>match.start()		   
4
>>>match.end()		   
8
>>>match.span()		   
(4, 8)
>>>match = re.match(r"[0-9]*[1-9][0-9]*","abcd1234")	   
>>>match.group(0) if match else "不匹配"
'不匹配'
>>> type(match)	   
<class 'NoneType'>
>>> match.string   
Traceback (most recent call last):
  File "<pyshell#112>", line 1, in <module>
    match.string
AttributeError: 'NoneType' object has no attribute 'string'
>>>re.findall(r"[0-9]*[1-9][0-9]*","abcd1234ijk456xyz987")	   
['1234', '456', '987']
>>>re.split(r"[0-9]*[1-9][0-9]*","abcd1234ijk456xyz987")		   
['abcd', 'ijk', 'xyz', '']
>>>re.sub(r"[0-9]*[1-9][0-9]*","替换","abcd1234ijk456xyz987")		   
'abcd替换ijk替换xyz替换'
>>>pat = re.compile(r"[0-9]*[1-9][0-9]*")		   
>>>match = pat.search("abcd1234")		   
>>>match.group(0) if match else "不匹配"		   
'1234'
>>>match = pat.match("abcd1234")
>>>match.group(0) if match else "不匹配"
'不匹配'
>>>pat.findall("abcd1234ijk456xyz987")		   
['1234', '456', '987']
>>>pat.split("abcd1234ijk456xyz987")		   
['abcd', 'ijk', 'xyz', '']
>>>pat.sub("替换", "abcd1234ijk456xyz987")		   
'abcd替换ijk替换xyz替换'
>>>match = re.search(r"^[0-9]*[1-9][0-9]*","abcd1234")		   
>>>match.group(0) if match else "不匹配"		   
'不匹配'
>>>match = re.search(r"[0-9]*[1-9][0-9]*$","abcd1234")		   
>>>match.group(0) if match else "不匹配"		   
'1234'
小测验
请将如下代码粘贴至"提交代码"页面，"保存并提交评判"后查看结果。注意，此时代码不是交互模式，而是文件模式。 

import re
s = ''' 院长室…010-68915660 书记室…010-68918726 副院长室…010-68918977 \
        学院办公室…010-68914866 招生办公室…010-68913146 教学办公室…010-68918950 \
        学籍部…010-68918808
    '''
m = re.compile(r"\d{3}-\d{8}|\d{4}-\d{7}")
for m in m.finditer(s):
   if m:
      print(m.group(0))

习题讲解
【代码分析】

import re
s = ''' 院长室…010-68915660 书记室…010-68918726 副院长室…010-68918977 \
        学院办公室…010-68914866 招生办公室…010-68913146 教学办公室…010-68918950 \
        学籍部…010-68918808
    '''
m = re.compile(r"\d{3}-\d{8}|\d{4}-\d{7}")
for m in m.finditer(s):
   if m:
      print(m.group(0))
finditer()函数将返回一个由match对象组成的迭代类型，与for...in...搭配使用遍历每一个匹配的match结果。

常用标准库之os/sys小练习
描述
这是一个关于"常用标准库之os/sys"的小练习，覆盖os库和sys库的基本操作，包含两部分内容：跟随练习 和 小测验。

在"跟随练习"环节，请使用IDLE编辑器的交互模式，逐一输入以下语句，观察并比较输出结果。

在"小测验"环节，请在本题目对应的"提交代码"页面按要求输入代码，"保存并提交评判"后查看结果。

跟随练习
 请使用IDLE编辑器的交互模式（含有>>>提示符），按顺序逐一输入以下语句（共20个）：

>>>import os
>>>os.getcwd()		   
'C:\\Users\\Tian Song\\AppData\\Local\\Programs\\Python\\Python36-32'
>>>os.getlogin()		   
'Tian Song'
>>>os.cpu_count()		   
8
>>>os.urandom(10)		   
b'K\xc3\xe6\x1c\xb2\xb1\xae=\x86\x1f'
>>>os.system("C:/Windows/system32/calc.exe")		   
0
>>>os.path.isfile("C:/Windows/system32/calc.exe")		   
True		   
>>>os.path.isdir("C:/Windows/system32/calc.exe")		   
False
>>>os.path.isdir("C:/Windows/system32/")

>>>import sys	   
>>>sys.float_info		   
sys.float_info(max=1.7976931348623157e+308, max_exp=1024, max_10_exp=308, min=2.2250738585072014e-308, min_exp=-1021, min_10_exp=-307, dig=15, mant_dig=53, epsilon=2.220446049250313e-16, radix=2, rounds=1)
>>>sys.int_info		   
sys.int_info(bits_per_digit=15, sizeof_digit=2)
>>>sys.hash_info		   
sys.hash_info(width=32, modulus=2147483647, inf=314159, nan=0, imag=1000003, algorithm='siphash24', hash_bits=64, seed_bits=128, cutoff=0)
>>>sys.thread_info		   
sys.thread_info(name='nt', lock=None, version=None)
>>>sys.byteorder		   
'little'
>>>sys.executable		   
'C:\\Users\\Tian Song\\AppData\\Local\\Programs\\Python\\Python36-32\\pythonw.exe'
>>>sys.maxunicode		   
1114111
>>>sys.path		   
['C:/Users/Tian Song/AppData/Local/Programs/Python/Python36-32', 'C:\\Users\\Tian Song\\AppData\\Local\\Programs\\Python\\Python36-32\\Lib\\idlelib', 'C:\\Users\\Tian Song\\AppData\\Local\\Programs\\Python\\Python36-32\\python36.zip', 'C:\\Users\\Tian Song\\AppData\\Local\\Programs\\Python\\Python36-32\\DLLs', 'C:\\Users\\Tian Song\\AppData\\Local\\Programs\\Python\\Python36-32\\lib', 'C:\\Users\\Tian Song\\AppData\\Local\\Programs\\Python\\Python36-32', 'C:\\Users\\Tian Song\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages', 'C:\\Users\\Tian Song\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\win32', 'C:\\Users\\Tian Song\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\win32\\lib', 'C:\\Users\\Tian Song\\AppData\\Local\\Programs\\Python\\Python36-32\\lib\\site-packages\\Pythonwin']
>>>sys.getrecursionlimit()		   
1000
>>>sys.getdefaultencoding()		   
'utf-8'
小测验
请将如下代码粘贴至"提交代码"页面，"保存并提交评判"后查看结果。注意，此时代码不是交互模式，而是文件模式。 

import os
import time
s = os.path.getctime("/bin/python3.6")
print(time.ctime(s))

习题讲解
【代码分析】

import os
import time
s = os.path.getctime("/bin/python3.6")
print(time.ctime(s))
getctime()函数将返回文件创建的时间，该时间是浮点数（时间戳）形式的表示。

随机字符串
描述
输入两个整数，以它们的和为随机数种子，并在32-127之间(含)随机产生20个整数。

以这些数字为Unicode码产生字符，并将组成字符串输出。 

输入格式
两个逗号分隔的整数。

输出格式
一个20个字符的字符串。

输入输出示例
 

 	输入	输出
示例 1	
1,2
>ke0Om\pj(m!\Af=8{\e

习题讲解
【参考代码】

import random
a, b = eval(input())
s = ""
random.seed(a+b)
for i in range(20):
    s += chr(random.randint(32, 127))
print(s)
random.randint(a,b)产生在[a,b]之间的一个随机整数。

时间差之天数计算
描述
获得用户输入的两个与时间相关的字符串，两个时间用逗号分隔，每个时间字符串格式示例如下：2018年08月01日17点21分21秒。

计算两个时间差的绝对值，输出相差的完整天数。

输入格式
一个包含两段时间的字符串。

输出格式
时间相差的天数

输入输出示例
 

 	输入	输出
示例 1	
2018年10月10日17点18分20秒,2018年10月11日16点18分20秒
1

时间差之天数计算  
习题讲解
【参考代码】

import time
ls = input().split(",")
ta = time.strptime(ls[0], "%Y年%m月%d日%H点%M分%S秒")
tb = time.strptime(ls[1], "%Y年%m月%d日%H点%M分%S秒")
print(int(abs(time.mktime(ta)-time.mktime(tb))//(3600*24)))
time.strptime(s, tpl)把字符串s按照tpl格式转变成struct_time格式，time.mktime(t)把struct_time格式时间t转变成浮点数形式时间。

系统信息获取
描述
获取系统中CPU个数、系统递归深度、当前执行文件路径、当前系统字节序标识（大端用big、小端用little）、系统最大UNICODE编码值等5个信息，并打印输出。

输出格式如下：

CPU:<个数>, RECLIMIT:<深度>, EXEPATH:<文件路径>, ENDIAN:<字节序>, UNICODE:<最大编码值>

输入格式
无。

输出格式
一个字符串。

输入输出示例
这里仅是格式参考，非正确答案。

 	输入	输出
示例 1	
无
CPU:4, RECLIMIT:500, EXEPATH:/bin/python, ENDIAN:big, UNICODE:1411

习题讲解
【参考代码】

import os, sys
print("CPU:{}, RECLIMIT:{}, EXEPATH:{}, ENDIAN:{}, UNICODE:{}".format(os.cpu_count(), sys.getrecursionlimit(), sys.executable, sys.byteorder, sys.maxunicode))
该实例利用了os库和sys库的相关函数或参数。

三文件比较
描述
附件提供了3个文件，名称分别是：file1.txt, file2.txt和file3.txt。

请编写程序，比较3个文件并输入文件的异同，每两个文件比较结果为一行。

输入格式
附件提供的3个文件。

输出格式
共3行输出结果，如下，其中"相同"可能被替换为"不相同"：

file1.txt与file2.txt相同

file1.txt与file3.txt不相同

file2.txt与file3.txt不相同

输入输出示例
这里是一个格式示例，不代表正确结果。

 	输入	输出
示例 1	
无
file1.txt与file2.txt相同
file1.txt与file3.txt不相同
file2.txt与file3.txt不相同
 

附件
序号
名称 程序内使用说明
1
file1.txt
2
file2.txt
3
file3.txt

习题讲解
【参考代码】

import filecmp
nls = ["file1.txt", "file2.txt", "file3.txt"]
for i in range(len(nls)):
    for j in range(i+1, len(nls)):
        print("{}与{}{}".format(nls[i], nls[j], "相同"if filecmp.cmp(nls[i], nls[j]) else "不相同"))
filecmp.cmp(f1, f2)可以进行两两文件比较，注意，采用双重循环遍历列表，两两比较元素，这个方法需要掌握。

匹配正则表达式
描述
给定一个正则表达式，如下：

      [1-9]\d{5}

请获得输入的字符串，提取其中所有匹配字符串，采用逗号分隔组成一个字符串输出。

输入格式
一个字符串文本。

输出格式
逗号分隔的字符串。

输入输出示例
 

 	输入	输出
示例 1	
北京理工大学100081 清华大学100084
100081,100084

习题讲解
【参考代码】

import re
s = input()
regex = re.compile(r"[1-9]\d{5}")
ls = regex.findall(s.strip("\n"))
print(",".join(ls))
findall()方法或函数能够将字符串中所有匹配提取出来，组成一个列表。

