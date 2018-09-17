时间差之分钟计算
描述
获得用户输入的两个与时间相关的字符串，两个时间用逗号分隔，每个时间字符串格式示例如下：2018-08-01 17:21:21。

计算两个时间差的绝对值，输出相差的完整分钟数。

输入格式
一个包含两段时间的字符串。

输出格式
时间相差的分钟数

输入输出示例
 

 	输入	输出
示例 1	
2018-10-10 17:18:20,2018-10-11 19:18:20
1560

import time
ls = input().split(",")
ta = time.strptime(ls[0], "%Y-%m-%d %H:%M:%S")
tb = time.strptime(ls[1], "%Y-%m-%d %H:%M:%S")
print(int(abs(time.mktime(ta)-time.mktime(tb))//60))

十文件比较
描述
附件提供了10个文件，名称分别是：file1.txt, file2.txt, ...., file10.txt。

请编写程序，比较10个文件并输入文件的异同，每两个文件比较结果为一行。

输入格式
附件提供的10个文件。

输出格式
每个比较一行输出结果，如下，其中"相同"可能被替换为"不相同"：

file1.txt与file2.txt相同

file1.txt与file3.txt不相同

file1.txt与file4.txt不相同

......

file2.txt与file3.txt不相同

......

 

输入输出示例
这里是一个格式示例，不代表正确结果。

 	输入	输出
示例 1	
无
file1.txt与file2.txt相同
file1.txt与file3.txt不相同
......
 

附件
序号
名称 程序内使用说明
1
file1.txt
2
file2.txt
3
file3.txt
4
file4.txt
5
file5.txt
6
file6.txt
7
file7.txt
8
file8.txt
9
file9.txt
10
file10.txt

import filecmp
nls = ["file1.txt", "file2.txt", "file3.txt", "file4.txt", "file5.txt", "file6.txt", "file7.txt", "file8.txt", "file9.txt", "file10.txt"]
for i in range(len(nls)):
    for j in range(i+1, len(nls)):
        print("{}与{}{}".format(nls[i], nls[j], "相同"if ilecmp.cmp(nls[i], nls[j]) else "不相同"))

正则表达式匹配
描述
给定一个正则表达式，如下：

      [1-9]\d{5}

请获得输入的字符串，提取其中所有匹配字符串，对于每个匹配结果按照一行输出，包括：匹配字符串、在原字符串中的起始位置和结束位置，格式如下：

<匹配字符串>:<起始位置>,<结束位置>

输入格式
一个字符串文本。

输出格式
多行的字符串。

输入输出示例
 

 	输入	输出
示例 1	
北京理工大学100081 清华大学100084
100081:6,12
100084:17,23

import re
s = input()
regex = re.compile(r"[1-9]\d{5}")
ls = regex.findall(s.strip("\n"))
for i in ls:
    mat = regex.search(s.strip("\n"))
    st = mat.start()
    ed = mat.end()
    print("{}:{},{}".format(i,st,ed))
