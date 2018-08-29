组合数据类型之集合小练习
描述
这是一个关于"组合数据类型之集合"的小练习，覆盖集合类型的基本、操作符、函数和方法等的使用，包含两部分内容：跟随练习 和 小测验。

在"跟随练习"环节，请使用IDLE编辑器的交互模式，逐一输入以下语句，观察并比较输出结果。

在"小测验"环节，请在本题目对应的"提交代码"页面按要求输入代码，"保存并提交评判"后查看结果。

跟随练习
 请使用IDLE编辑器的交互模式（含有>>>提示符），按顺序逐一输入以下语句（共20个）：

>>>d = set()
>>>e = {1, 1, 2, 2, 3, 3}
>>>print(d, e)
set() {1, 2, 3}
>>>d.add(4)
>>>d.update({2, 3})
>>>d
{2, 3, 4}
>>>d.intersection(e)
{2, 3}
>>>d.union(e)
{1, 2, 3, 4}
>>>d.difference(e)
{4}
>>>d.symmetric_difference(e)
{1, 4}
>>>d.intersection_update(e)
>>>d
{2, 3}
>>>len(d)
2
>>>d.remove(3)
>>>d
{2}
>>>d.discard(3)
>>>d
{2}
>>>d.discard(2)
>>>d.pop()
Traceback (most recent call last):
  File "<pyshell#33>", line 1, in <module>
    d.pop()
KeyError: 'pop from an empty set'
>>>d.issubset(e)
True
小测验
请将如下代码粘贴至"提交代码"页面，"保存并提交评判"后查看结果。注意，此时代码不是交互模式，而是文件模式。 

d = {"a", "b", "c", "d"}
e = {"b", "c", "d", "e"}
for op in ["d&e", "d|e", "d-e", "d^e"]:
    ls = list(eval(op))
    ls.sort()
    print(ls, end="  ")

    习题讲解
【代码分析】

d = {"a", "b", "c", "d"}
e = {"b", "c", "d", "e"}
for op in ["d&e", "d|e", "d-e", "d^e"]:
    ls = list(eval(op))
    ls.sort()
    print(ls, end="  ")
此代码训练了集合类型的四种运算：交并差补，&|-^四个符号比较好理解。如果希望更新d，可以用如下表达式：

d &= e
d |= e
d -= e
d ^= e

组合数据类型之元组小练习
描述
这是一个关于"组合数据类型之元组"的小练习，覆盖元组类型的基本、操作符、函数和方法等的使用，包含两部分内容：跟随练习 和 小测验。

在"跟随练习"环节，请使用IDLE编辑器的交互模式，逐一输入以下语句，观察并比较输出结果。

在"小测验"环节，请在本题目对应的"提交代码"页面按要求输入代码，"保存并提交评判"后查看结果。

跟随练习
 请使用IDLE编辑器的交互模式（含有>>>提示符），按顺序逐一输入以下语句（共20个）：

>>>t = 1, 2, 3, 2, 1
>>>max(t)
3
>>>t.index(1)
0
>>>t.count(1)
2
>>>s = (1, "a", 2, "b")
>>>min(s)
Traceback (most recent call last):
  File "<pyshell#49>", line 1, in <module>
    min(s)
TypeError: unorderable types: str() < int()
>>>t + s
(1, 2, 3, 2, 1, 1, 'a', 2, 'b')
>>>print(t, s)
(1, 2, 3, 2, 1) (1, 'a', 2, 'b')
>>>t2 = tuple(set(t))
>>>print(t, t2)
(1, 2, 3, 2, 1) (1, 2, 3)
>>>len(t)
5
>>>t > t2
True
>>>t3 = t2*3
>>>print(t2, t3)
(1, 2, 3) (1, 2, 3, 1, 2, 3, 1, 2, 3)
>>>t3[::3]
(1, 1, 1)
>>>t3[::-1]
(3, 2, 1, 3, 2, 1, 3, 2, 1)
>>>t2 in t3
False
>>>2, 3 in t3
(2, True)
>>>p = 1, 2, [1,2]
(1, 2, [1, 2])
>>> p[-1]
[1, 2]
小测验
请将如下代码粘贴至"提交代码"页面，"保存并提交评判"后查看结果。注意，此时代码不是交互模式，而是文件模式。 

t = 1, 2, 3, [1, 2, 3]
try:
   t[-1].extend([4, 5, 6])
   print(t)
except:
   print("error")

   习题讲解
【代码分析】

t = 1, 2, 3, [1, 2, 3]
try:
   t[-1].extend([4, 5, 6])
   print(t)
except:
   print("error")
在定义元组时，列表可以作为其元素，实际上是列表的指针是其元素。所以，元组要求其元素不能修改，只要列表指针不修改即可。因此，这里见到了一种"奇怪"的现象，元组元素的"值"可以被修改，请大家合理理解这个现象。

组合数据类型之列表小练习
描述
这是一个关于"组合数据类型之列表"的小练习，覆盖列表类型的基本、操作符、函数和方法等的使用，包含两部分内容：跟随练习 和 小测验。

在"跟随练习"环节，请使用IDLE编辑器的交互模式，逐一输入以下语句，观察并比较输出结果。

在"小测验"环节，请在本题目对应的"提交代码"页面按要求输入代码，"保存并提交评判"后查看结果。

跟随练习
 请使用IDLE编辑器的交互模式（含有>>>提示符），按顺序逐一输入以下语句（共30个）：

>>>ls = [1, 2, 1, "a", "b", "a"]
>>>ls[::-2]
['a', 'a', 2]
>>>"b" in ls
True
>>>del ls[-2]
>>>ls
[1, 2, 1, 'a', 'a']
>>>len(ls)
5
>>>print(list(set(ls)))
[1, 2, 'a']
>>>ls.append(["b", "c"])
>>>ls.insert(3, (1, 2))
>>>ls
[1, 2, 1, (1, 2), 'a', 'a', ['b', 'c']]
>>>lt = ["d", "e"]
>>>ls.extend(lt)
>>>ls
[1, 2, 1, (1, 2), 'a', 'a', ['b', 'c'], 'd', 'e']
>>>ls.remove('a')
>>>ls
[1, 2, 1, (1, 2), 'a', ['b', 'c'], 'd', 'e']
>>>ls.pop(5)
['b', 'c']
>>>ls
[1, 2, 1, (1, 2), 'a', 'd', 'e']
>>>ls.count(1)
2
>>>ls.index('a')
4
>>>ls.reverse()
>>>ls
['e', 'd', 'a', (1, 2), 2, 1, 1]
>>>lt = ls
>>>lt.remove('e')
>>>lt.remove('d')
>>>print(ls, lt)
['a', (1, 2), 2, 1, 1] ['a', (1, 2), 2, 1, 1]
>>>lt2 = ls.copy()
>>>lt2.remove('a')
>>>print(ls, lt, lt2)
['a', (1, 2), 2, 1, 1] ['a', (1, 2), 2, 1, 1] [(1, 2), 2, 1, 1]
>>>ls.clear()
>>>print(ls, lt, lt2)
[] [] [(1, 2), 2, 1, 1]
小测验
请将如下代码粘贴至"提交代码"页面，"保存并提交评判"后查看结果。注意，此时代码不是交互模式，而是文件模式。 

ls = [1, 3, 5, 7, 9, 8, 6, 4, 2, 0]
lt = ["cat", "mouse", "zebra", "snake", "panda"]
for c in (ls, lt):
    c.sort()
    print(c)

习题讲解
【代码分析】

ls = [1, 3, 5, 7, 9, 8, 6, 4, 2, 0]
lt = ["cat", "mouse", "zebra", "snake", "panda"]
for c in (ls, lt):
    c.sort()
    print(c)
列表sort()方法能够按照默认从小到大顺序对元素进行排序，并且改变列表内容。对于字符串，采用字符Unicode码顺序进行排序。

组合数据类型之字典小练习
描述
这是一个关于"组合数据类型之字典"的小练习，覆盖字典类型的基本、操作符、函数和方法等的使用，包含两部分内容：跟随练习 和 小测验。

在"跟随练习"环节，请使用IDLE编辑器的交互模式，逐一输入以下语句，观察并比较输出结果。

在"小测验"环节，请在本题目对应的"提交代码"页面按要求输入代码，"保存并提交评判"后查看结果。

跟随练习
 请使用IDLE编辑器的交互模式（含有>>>提示符），按顺序逐一输入以下语句（共30个）：

>>>d = {}
>>>d["a"] = 1
>>>d.update({"b":2, "c":3})
>>>d
{'b': 2, 'a': 1, 'c': 3}
>>>d['c']
3
>>>d.get('e')
>>>d.get('c')
3
>>>d.get('c', 100)
3
>>>d.get('e', 100)
100
>>>d.keys()
dict_keys(['b', 'a', 'c'])
>>>type(d.keys())
<class 'dict_keys'>
>>>d.values()
dict_values([2, 1, 3])
>>>d.items()
dict_items([('b', 2), ('a', 1), ('c', 3)])
>>>ld = list(d.items())
>>>ld
[('b', 2), ('a', 1), ('c', 3)]
>>>ld[-1][-1]
3
>>>d.pop('a')
1
>>>d
{'b': 2, 'c': 3}
>>>d.popitem()
('b', 2)
>>>d
{'c': 3}
>>>'c' in d
True
>>>len(d)
1
>>>del d['c']
>>>d
{}
>>>d = dict([('a', 1),('b', 2),('c', 3)])
>>>d
{'c': 3, 'a': 1, 'b': 2}
>>>e = dict((('a', 1),('b', 2),('c', 3)))
>>>e
{'c': 3, 'a': 1, 'b': 2}
>>>d > e
Traceback (most recent call last):
  File "<pyshell#44>", line 1, in <module>
    d > e
TypeError: unorderable types: dict() > dict()
>>>d == e
True
小测验
请将如下代码粘贴至"提交代码"页面，"保存并提交评判"后查看结果。注意，此时代码不是交互模式，而是文件模式。 

s = "a b a b c a b c"
d = {}
for c in s.split():
    d[c] = d.get(c, 0) + 1
print(d)

习题讲解
【代码分析】

s = "a b a b c a b c"
d = {}
for c in s.split():
    d[c] = d.get(c, 0) + 1
print(d)
字典get(key, default)方法能够获得字典key对应的值，如果key:value在字典中不存在，则返回default值。

理解Python之禅
描述
Python语言解释器安装文件自带了一个this.py文件，解释了Python之禅，调用该库及输出内容如下（嵩老师教材里面有对应的中文翻译）：

>>> import this
The Zen of Python, by Tim Peters

Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.
Special cases aren't special enough to break the rules.
Although practicality beats purity.
Errors should never pass silently.
Unless explicitly silenced.
In the face of ambiguity, refuse the temptation to guess.
There should be one-- and preferably only one --obvious way to do it.
Although that way may not be obvious at first unless you're Dutch.
Now is better than never.
Although never is often better than *right* now.
If the implementation is hard to explain, it's a bad idea.
If the implementation is easy to explain, it may be a good idea.
Namespaces are one honking great idea -- let's do more of those!
在Python解释器安装目录中能够找到this.py文件，其内容如下：

s = """Gur Mra bs Clguba, ol Gvz Crgref

Ornhgvshy vf orggre guna htyl.
Rkcyvpvg vf orggre guna vzcyvpvg.
Fvzcyr vf orggre guna pbzcyrk.
Pbzcyrk vf orggre guna pbzcyvpngrq.
Syng vf orggre guna arfgrq.
Fcnefr vf orggre guna qrafr.
Ernqnovyvgl pbhagf.
Fcrpvny pnfrf nera'g fcrpvny rabhtu gb oernx gur ehyrf.
Nygubhtu cenpgvpnyvgl orngf chevgl.
Reebef fubhyq arire cnff fvyragyl.
Hayrff rkcyvpvgyl fvyraprq.
Va gur snpr bs nzovthvgl, ershfr gur grzcgngvba gb thrff.
Gurer fubhyq or bar-- naq cersrenoyl bayl bar --boivbhf jnl gb qb vg.
Nygubhtu gung jnl znl abg or boivbhf ng svefg hayrff lbh'er Qhgpu.
Abj vf orggre guna arire.
Nygubhtu arire vf bsgra orggre guna *evtug* abj.
Vs gur vzcyrzragngvba vf uneq gb rkcynva, vg'f n onq vqrn.
Vs gur vzcyrzragngvba vf rnfl gb rkcynva, vg znl or n tbbq vqrn.
Anzrfcnprf ner bar ubaxvat terng vqrn -- yrg'f qb zber bs gubfr!"""

d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))
请阅读这段代码，并理解其中最后6行代码。这段代码是一个密码算法，请默写这段代码完整加解密功能。

输入格式
一段文本，明文或密文。

输出格式
一段文本，密文或明文。

输入输出示例
 	输入	输出
示例 1	
abcdefghijklmnopqrstuvwxyz
nopqrstuvwxyzabcdefghijklm

习题讲解
【参考代码】

s = input()
d = {}
for c in (65, 97):
    for i in range(26):
        d[chr(i+c)] = chr((i+13) % 26 + c)

print("".join([d.get(c, c) for c in s]))
请理解并熟记这段代码。

列表非同个数计算
描述
获得用户输入的一个列表元素，输出其包含值不同元素的个数。

输入格式
一个具体的列表值。

输出格式
整数

输入输出示例
 

 	输入	输出
示例 1	
[0, 1, 2, 3, 4, 4.0, 4.00, 3, 2, 1, 0]
5

习题讲解
【参考代码】

ls = eval(input())
try:
    print(len(set(ls)))
except:    #无法用set去重
    count = 0
    for item in ls:
        count += 1 / ls.count(item)
    print(round(count))
尽管将列表转换成集合能够去重，但由于集合要求元素必须可哈希，所以，并非所有列表都能转换为集合。采用try-except应对这种情况。

文本输入统计
描述
输入一段由空格分隔的文本，统计本文中每个单词出现的次数，并以单词:次数形式打印输出。

输入格式
一段文本

输出格式
单词:次数，其中，次数为整数，所有单词按照字母序排列。

输入输出示例
 

 	输入	输出
示例 1	
Alice
Bob
hello Alice
hello Bob
 
习题讲解
【参考代码】

txt = input()
d = {}
for w in txt.split():
    d[w] = d.get(w, 0) + 1 
ls = list(d.items())
ls.sort()
for w, c in ls:
    print("{}:{}".format(w,c))
将字典转换为列表及排序的方法。

文本字符分布
描述
分析附件data.txt文件的字符分布，即每个字符对应的数量。

按照 字符:数量 显示，每行一个结果，如果没有出现该字节则不显示输出，字符采用Unicode编码升序排列。

输入格式
data.txt文件

输出格式
字符:数量，其中，字符表示为可打印字符，按照升序。

输入输出示例
这里仅提供一个格式参考，非答案。

 	输入	输出
示例 1	
(读入文件)
a:1
b:2
c:3
 

附件
序号
名称 程序内使用说明
1
data.txt

习题讲解
【参考代码】

f = open("data.txt")
txt = f.read()
d = {}
for w in txt:
    d[w] = d.get(w,0) + 1
ls = list(d.items())
ls.sort()
for k, c in ls:
    print("{}:{}".format(k, c))
f.close()
采用字典进行字符或单词统计是经典方法，务必熟练掌握。

文本字节分布
描述
分析附件data.txt文件的字节分布，即每个字节对应的数量。

按照 字节:数量 显示，每行一个结果，如果没有出现该字节则不显示输出，字节表示为00到FF。

输入格式
data.txt文件

输出格式
字节:数量，其中，字节表示为00到FF，按照升序，不出现不显示。

输入输出示例
这里仅提供一个格式参考，非答案。

 	输入	输出
示例 1	
(读入文件)
00:1
0F:2
FA:3
 

附件
序号
名称 程序内使用说明
1
data.txt

习题讲解
【参考代码】

f = open("data.txt", "rb")
btxt = f.read()
ls = [0 for c in range(256)]
for b in btxt:
    ls[b] += 1
for i in range(len(ls)):
    if ls[i] != 0:
        print("{:02X}:{}".format(i, ls[i]))
f.close()
注意区别字符串和字节串，从文件获得字节串需要使用二进制方式打开。




