WordCloud词云生成 II
描述
wordcloud是生成词云的Python第三方库，也是Python优秀的计算生态之一。

下面是一段生成词云的代码，但这段代码并不能如期产生理想的词云效果。请在不改变代码行数的情况下，修改代码，达到生成理想词云的目的。

import wordcloud, jieba
c = wordcloud.WordCloud(font_path="msyh.ttc")
s = "新时代中国特色社会主义思想是全党全国人民为实现中华民族伟大复兴而奋斗的行动指南"
c.generate(s)
c.to_file("outfile.png")
词云的参考效果如下：



请将修改后的代码打印输出。

输入格式

无

输出格式
一行替换原有代码的代码

输入输出示例
这里仅提供输出格式样例

 	输入	输出
示例 1	
无
print("Hello World")

import wordcloud, jieba
c = wordcloud.WordCloud(font_path="msyh.ttc")
s = "新时代中国特色社会主义思想是全党全国人民为实现中华民族伟大复兴而奋斗的行动指南"
c.generate(s)
c.to_file("outfile.png")

《白鹿原》之长度N单词统计
描述
附件是《白鹿原》原著内容，请读入内容，分词后输出长度为N的不同单词的个数，其中N为用户输入的整数。

统计时，相同单词总计为1次。

输入格式
文件及用户输入

输出格式
整数

输入输出示例
仅提供一个输出示范样例。

 	输入	输出
示例 1	
3
4287
 

附件
序号
名称 程序内使用说明
1
白鹿原.txt


二维数据表格输出 II
描述
tabulate能够对二维数据进行表格输出，是Python优秀的第三方计算生态。

参考编程模板中给定的数据和代码，编写程序，能够输出如下风格效果的表格数据。

 

输入格式
参考编程模板中部分代码

输出格式
参考上图中效果

 from tabulate import tabulate
data = [ ["北京理工大学", "985", 2000], \
         ["清华大学", "985", 3000], \
         ["大连理工大学", "985", 4000], \
         ["深圳大学", "211", 2000], \
         ["沈阳大学", "省本", 2000], \
    ]
print(tabulate(data, tablefmt="rst"))