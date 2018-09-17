1. 关于pip指令，以下能够下载但不安装第三方库安装文件的是：
A
pip list <第三方库名>
B
pip uninstall <第三方库名>
C
pip download <第三方库名>
D
pip search <第三方库名>
 正确答案： C 
pip download <第三方库名> 可用于提前下载拟安装库文件，并向未能联网计算机安装提供支持。



2. 以下对UCI安装方法说明错误的是：
A
UCI方法下载的文件不能用pip进行安装
B
UCI方法适用于Windows平台
C
UCI是加州大学尔湾分校的简写
D
UCI方法针对少量第三方库，提供编译后的版本供下载安装
 正确答案： A 
UCI方法下载后的文件使用pip install <下载文件全名>进行安装。



3. 关于PyInstaller库，以下能够为其指定图标文件的选项是：
A
-F
B
-i
C
-n
D
--distpath
 正确答案： B 
PyInstaller库指定图标的方法是：pyinstaller -i <图标文件> a.py



4. 以下表示全模式分词且返回列表类型的函数是：
A
jieba.lcut(s, cut_all=True)
B
jieba.lcut_for_search(s, cut_all=True)
C
jieba.lcut_all(s)
D
jieba.lcut(s)
 正确答案： A 
jieba库一共提供jieba.cut()、jieba.lcut()、jieba.cut_for_search()、jieba.lcut_for_search()四个与分词相关的函数，其中jieba.lcut(s, cut_all = True)是全模式分词。



5. 以下不属于wordcloud生成词云三个步骤函数的是：
A
c.draw()
B
c = wordcloud.WordCloud()
C
c.generate(txt)
D
c.to_file("output.png")
 正确答案： A 
wordcloud库三个步骤的实例代码如下：

import wordcloud
c = wordcloud.WordCloud()
c.generate("One Python, One World")
c.to_file("outfile.png")


6. 关于pipevn库，以下是其管理虚拟环境所使用文件的是：
A
list.lock
B
pipenv
C
lock.Pipfile
D
Pipfile
 正确答案： D 
pipenv使用Pipfile和Pipefile.lock两个文件来管理虚拟环境。



7. 以下不能用于tabulate库优美打印的数据据类型是：
A
numpy的二维数组
B
二维列表
C
pandas库的DataFrame类型
D
字符串
 正确答案： D 
tabulate库可以支持二维列表、二维迭代类型、字典迭代、NumPy二维数组、pandas库DataFrame类型的格式化输出。



8. 关于QRcode库，以下能够生成二维码的函数是：
A
qrcode.generate(txt)
B
qrcode.image(txt)
C
qrcode.make(txt)
D
qrcode.save()
 正确答案： C 
QRcode库只有一个二维码生成函数  qrcode.make(txt)。



9. 关于Python计算生态，以下理解错误的是：
A
Python计算生态没有顶层设计
B
第三方库受开发者的影响很大
C
所有标准库使用风格都比较接近
D
第三方库的使用方法大都不一样
 正确答案： C 
Python计算生态没有顶层设计，各库使用方法都不相同。



10. Python计算生态超过14万个，以下能帮助学习者更明智学习Python的方法是：
A
观察周围学习者学习什么，跟着学习
B
多花时间实践，遇到案例就去练习
C
多花时间学习，遇到Python知识就去学习
D
学好Python语法，有选择有判断地选学标准库和第三方库
 正确答案： D 
Python计算生态的庞大性已经超过一般人能接受的范畴，一定要学会思考和判断，将有限精力投入到关键和必要的内容学习中，不要盲目跟风，可能周围人未必对Python有正确认识。