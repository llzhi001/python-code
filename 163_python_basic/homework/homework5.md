1. 以下描述了Python标准库和第三方库区别的是：
标准库在Python解释器安装后可以直接使用
标准库稳定性更好
对于特定功能，如时间处理，标准库提供独一无二的库
标准库由Python社区核心团队编写
 正确答案： A 
标准库与第三方库的核心区别是：标准库由Python解释器自带，安装后可以直接使用



2. 以下对PYPI描述错误的是：
PYPI为第三方库提供了文档、代码维护和下载等功能
PYPI提供了搜索及分类检索第三方库的功能
PYPI的地址是：https://pypi.org
PYPI全称是：Python Package Index
 正确答案： A 
PYPI上不提供第三方库的源代码和文档



3. 以下不是Python计算生态特点的是：
相互依存
统筹规划
迅速更迭
竞争发展
 正确答案： B 
Python计算生态类似自然生态，无顶层设计和统筹规划，任何表现为"貌似"规划的现象都是竞争发展的结果。



4. 以下能够返回struct_time类型时间的函数是：
time.asctime()
time.mktime()
time.gmtime()
time.time()
 正确答案： C 
能够返回struct_time类型时间的函数是：time.gmtime()和time.localtime()



5. 以下能够返回随机整数的函数是：
random.uniform()
random.randrange()
random.random()
random.sample()
 正确答案： B 
能够返回随机整数的函数是：random.randint()、random.randrange()、random.getrandbits()。



6. 对于正则表达式re库，以下返回match对象的函数是：
re.search()
re.split()
re.findall()
re.sub()
 正确答案： A 
在re库中，返回match对象的函数有：re.search()、re.match()、re.finditer()。



7. 以下能够获得文件最近一次被修改时间的函数是：
os.path.getmtime()
os.path.getatime()
os.path.isfile()
os.path.getctime()
 正确答案： A 
os.path.getatime()：获得文件最后一次访问时间

os.path.getmtime()：获得文件最后一次被修改时间

os.path.getctime()：获得文件创建时间



8. 关于filecmp库，用来比较两个目录的对象是：
filecmp.cmpfiles()
filecmp.dircmp()
filecmp.cmpdirs()
filecmp.cmp()
 正确答案： B 
cmpfile库采用cmpfile.dircmp()对象来比较目录，相比，采用filecmp.cmpfiles()比较文件。



9. 以下能够获得命令行参数的是：
sys.argv
sys.exit()
sys.getsizeof()
sys.path
 正确答案： A 
sys.argv获得命令行参数，其中sys.argv[0]是Python执行程序（命令）本身。



10.
这里是某程序代码片段，以下不属于该程序能够接受的参数是：

import getopt
...
getopt.getopt(sys.argv[1:], "hi:vf", ["dir=", "clean"])
...
--dir <目录名>

-f <文件名>

-v

-h

 正确答案： B 
getopt库中的getopt()函数用来定义命令行参数，其中"abc:d:"中，带有冒号的后面可以接参数，否则不接参数。