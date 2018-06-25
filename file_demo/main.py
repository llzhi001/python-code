#coding=utf-8

#1.打开一个文件
#2.写入一些内容
#3.关闭文件

#w: write
#file pointer 文件指针

# fp = open('test.txt','a')
# #fp.write('hello world!!!!')
# fp.close()
#
# fp = open('test.txt','r')
# #content = fp.read(5)
# #content = fp.readline()
# #print(content)
# content = fp.readlines()
# for line in content:
#     print(line,end='')
#
# fp.close()

import os

#1.文件重命名
#os.rename('test.txt','text.txt')

#2.删除文件
#os.remove('text.txt')

#3.获取当前目录
path = os.getcwd()
print(path)

#4.获取指定目录下的所有文件
file_list = os.listdir('.')
print(file_list)