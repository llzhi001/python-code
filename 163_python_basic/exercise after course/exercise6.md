常用第三方库之jieba/wordcloud小练习
描述
这是一个关于"常用第三方库之jieba/wordcloud"的小练习，覆盖jieba库和wordcloud库的基本操作，包含两部分内容：跟随练习 和 小测验。

在"跟随练习"环节，请使用IDLE编辑器的交互模式，逐一输入以下语句，观察并比较输出结果。

在"小测验"环节，请在本题目对应的"提交代码"页面按要求输入代码，"保存并提交评判"后查看结果。

跟随练习
 请使用IDLE编辑器的交互模式（含有>>>提示符），按顺序逐一输入以下语句（共30个）：

>>>s = "习近平总书记提出了新时代中国特色社会主义思想"

>>>import jieba

>>>jieba.lcut(s)

['习近平', '总书记', '提出', '了', '新', '时代', '中国', '特色', '社会主义', '思想']

>>>jieba.lcut_for_search(s)

['习近平', '书记', '总书记', '提出', '了', '新', '时代', '中国', '特色', '社会', '会主', '主义', '社会主义', '思想']

>>>jieba.lcut(s, cut_all = True)

['习近平', '总书记', '书记', '提出', '了', '新', '时代', '中国', '国特', '特色', '社会', '社会主义', '会主', '主义', '思想']

>>>for w in jieba.cut(s):
	print(w, end=",")
	
习近平,总书记,提出,了,新,时代,中国,特色,社会主义,思想,

>>>type(w)

<class 'str'>

>>>jieba.add_word("新时代中国特色社会主义")

>>>jieba.lcut(s)

['习近平', '总书记', '提出', '了', '新时代中国特色社会主义', '思想']

>>>jieba.add_word("新时代")

>>>jieba.lcut(s)

['习近平', '总书记', '提出', '了', '新时代中国特色社会主义', '思想']

>>>import os

>>>os.chdir("D:/")

>>>import wordcloud

>>>w = wordcloud.WordCloud()

>>>w.generate(s)

<wordcloud.wordcloud.WordCloud object at 0x000001E9B38161D0>

>>>w.to_file("wordcloud.png")

(在D盘根目录下查看生成的词云文件)

>>>w = wordcloud.WordCloud(font_path="msyh.ttc")

>>>w.generate(s)

<wordcloud.wordcloud.WordCloud object at 0x000001E9C6B68B70>

>>>w.to_file("wordcloud.png")

(在D盘根目录下查看生成的词云文件)

>>>w.generate(" ".join(jieba.lcut(s)))

<wordcloud.wordcloud.WordCloud object at 0x000001E9C6B68B70>

>>>w.to_file("wordcloud.png")

(在D盘根目录下查看生成的词云文件)

>>>w = wordcloud.WordCloud(font_path="msyh.ttc", width=1000, height=700)

>>>w.generate(" ".join(jieba.lcut(s)))

<wordcloud.wordcloud.WordCloud object at 0x000001E9C78F7FD0>

>>>w.to_file("wordcloud.png")

(在D盘根目录下查看生成的词云文件)

>>>w = wordcloud.WordCloud(font_path="msyh.ttc", background_color = "green")

>>>w.generate(" ".join(jieba.lcut(s)))

>>>w.to_file("wordcloud.png")

(在D盘根目录下查看生成的词云文件)

>>>w.generate("Python123 is a leading platform for Python programming")

<wordcloud.wordcloud.WordCloud object at 0x000001E9B3F82D68>

>>>w.to_file("wordcloud.png")
		     
(在D盘根目录下查看生成的词云文件)
小测验
请将如下代码粘贴至"提交代码"页面，"保存并提交评判"后查看结果。注意，此时代码不是交互模式，而是文件模式。 

import jieba
s = input()
ls = jieba.lcut_for_search(s)
lt = jieba.lcut(s)
for w in lt:
   ls.remove(w)
print(ls)

习题讲解
【代码分析】

import jieba
s = input()
ls = jieba.lcut_for_search(s)
lt = jieba.lcut(s)
for w in lt:
   ls.remove(w)
print(ls)
此代码比较了jieba中精确匹配lcut()和搜索匹配lcut_for_search()的分词结果。

常用第三方库之tabulate/QRcode小练习
描述
这是一个关于"常用第三方库之tabulate/QRcode"的小练习，覆盖tabulate库和QRcode库的基本操作，包含两部分内容：跟随练习 和 小测验。

在"跟随练习"环节，请使用IDLE编辑器的交互模式，逐一输入以下语句，观察并比较输出结果。

在"小测验"环节，请在本题目对应的"提交代码"页面按要求输入代码，"保存并提交评判"后查看结果。

跟随练习
 请使用IDLE编辑器的交互模式（含有>>>提示符），按顺序逐一输入以下语句（共50个）：

>>> from tabulate import tabulate

>>> data = []

>>> data.append(["北京大学","综合类","北京","本科一批"])

>>> data.append(["清华大学","综合类","北京","本科一批"])

>>> data.append(["浙江大学","综合类","浙江","本科一批"])

>>> data.append(["复旦大学","综合类","上海","本科一批"])

>>> data.append(["中国人民大学","综合类","北京","本科一批"])

>>> data.append(["上海交通大学","综合类","上海","本科一批"])

>>> data.append(["武汉大学","综合类","湖北","本科一批"])

>>> data.append(["南京大学","综合类","江苏","本科一批"])

>>> data.append(["中山大学","综合类","广东","本科一批"])

>>> data.append(["北京理工大学","理工类","北京","本科一批"])

>>> data

[['北京大学', '综合类', '北京', '本科一批'], ['清华大学'...(略)

>>> print(tabulate(data))

------  ---  --  ----
北京大学    综合类  北京  本科一批
清华大学    综合类  北京  本科一批
浙江大学    综合类  浙江  本科一批
复旦大学    综合类  上海  本科一批
中国人民大学  综合类  北京  本科一批
上海交通大学  综合类  上海  本科一批
武汉大学    综合类  湖北  本科一批
南京大学    综合类  江苏  本科一批
中山大学    综合类  广东  本科一批
北京理工大学  理工类  北京  本科一批
------  ---  --  ----

>>> hdls = ["学校", "类别", "地区", "招生批次"]

>>> print(tabulate(data, headers=hdls))

学校      类别    地区    招生批次
------  ----  ----  ------
北京大学    综合类   北京    本科一批
清华大学    综合类   北京    本科一批
浙江大学    综合类   浙江    本科一批
复旦大学    综合类   上海    本科一批
中国人民大学  综合类   北京    本科一批
上海交通大学  综合类   上海    本科一批
武汉大学    综合类   湖北    本科一批
南京大学    综合类   江苏    本科一批
中山大学    综合类   广东    本科一批
北京理工大学  理工类   北京    本科一批

>>> print(tabulate(data, headers=hdls, tablefmt="plain"))

学校      类别    地区    招生批次
北京大学    综合类   北京    本科一批
清华大学    综合类   北京    本科一批
浙江大学    综合类   浙江    本科一批
复旦大学    综合类   上海    本科一批
中国人民大学  综合类   北京    本科一批
上海交通大学  综合类   上海    本科一批
武汉大学    综合类   湖北    本科一批
南京大学    综合类   江苏    本科一批
中山大学    综合类   广东    本科一批
北京理工大学  理工类   北京    本科一批

>>> print(tabulate(data, headers=hdls, tablefmt="simple"))

学校      类别    地区    招生批次
------  ----  ----  ------
北京大学    综合类   北京    本科一批
清华大学    综合类   北京    本科一批
浙江大学    综合类   浙江    本科一批
复旦大学    综合类   上海    本科一批
中国人民大学  综合类   北京    本科一批
上海交通大学  综合类   上海    本科一批
武汉大学    综合类   湖北    本科一批
南京大学    综合类   江苏    本科一批
中山大学    综合类   广东    本科一批
北京理工大学  理工类   北京    本科一批

>>> print(tabulate(data, headers=hdls, tablefmt="grid"))

+--------+------+------+--------+
| 学校     | 类别   | 地区   | 招生批次   |
+========+======+======+========+
| 北京大学   | 综合类  | 北京   | 本科一批   |
+--------+------+------+--------+
| 清华大学   | 综合类  | 北京   | 本科一批   |
+--------+------+------+--------+
| 浙江大学   | 综合类  | 浙江   | 本科一批   |
+--------+------+------+--------+
| 复旦大学   | 综合类  | 上海   | 本科一批   |
+--------+------+------+--------+
| 中国人民大学 | 综合类  | 北京   | 本科一批   |
+--------+------+------+--------+
| 上海交通大学 | 综合类  | 上海   | 本科一批   |
+--------+------+------+--------+
| 武汉大学   | 综合类  | 湖北   | 本科一批   |
+--------+------+------+--------+
| 南京大学   | 综合类  | 江苏   | 本科一批   |
+--------+------+------+--------+
| 中山大学   | 综合类  | 广东   | 本科一批   |
+--------+------+------+--------+
| 北京理工大学 | 理工类  | 北京   | 本科一批   |
+--------+------+------+--------+

>>> print(tabulate(data, headers=hdls, tablefmt="fancy_grid"))

╒════════╤══════╤══════╤════════╕
│ 学校     │ 类别   │ 地区   │ 招生批次   │
╞════════╪══════╪══════╪════════╡
│ 北京大学   │ 综合类  │ 北京   │ 本科一批   │
├────────┼──────┼──────┼────────┤
│ 清华大学   │ 综合类  │ 北京   │ 本科一批   │
├────────┼──────┼──────┼────────┤
│ 浙江大学   │ 综合类  │ 浙江   │ 本科一批   │
├────────┼──────┼──────┼────────┤
│ 复旦大学   │ 综合类  │ 上海   │ 本科一批   │
├────────┼──────┼──────┼────────┤
│ 中国人民大学 │ 综合类  │ 北京   │ 本科一批   │
├────────┼──────┼──────┼────────┤
│ 上海交通大学 │ 综合类  │ 上海   │ 本科一批   │
├────────┼──────┼──────┼────────┤
│ 武汉大学   │ 综合类  │ 湖北   │ 本科一批   │
├────────┼──────┼──────┼────────┤
│ 南京大学   │ 综合类  │ 江苏   │ 本科一批   │
├────────┼──────┼──────┼────────┤
│ 中山大学   │ 综合类  │ 广东   │ 本科一批   │
├────────┼──────┼──────┼────────┤
│ 北京理工大学 │ 理工类  │ 北京   │ 本科一批   │
╘════════╧══════╧══════╧════════╛

>>> print(tabulate(data, headers=hdls, tablefmt="pipe"))

| 学校     | 类别   | 地区   | 招生批次   |
|:-------|:-----|:-----|:-------|
| 北京大学   | 综合类  | 北京   | 本科一批   |
| 清华大学   | 综合类  | 北京   | 本科一批   |
| 浙江大学   | 综合类  | 浙江   | 本科一批   |
| 复旦大学   | 综合类  | 上海   | 本科一批   |
| 中国人民大学 | 综合类  | 北京   | 本科一批   |
| 上海交通大学 | 综合类  | 上海   | 本科一批   |
| 武汉大学   | 综合类  | 湖北   | 本科一批   |
| 南京大学   | 综合类  | 江苏   | 本科一批   |
| 中山大学   | 综合类  | 广东   | 本科一批   |
| 北京理工大学 | 理工类  | 北京   | 本科一批   |

>>> print(tabulate(data, headers=hdls, tablefmt="orgtbl"))

| 学校     | 类别   | 地区   | 招生批次   |
|--------+------+------+--------|
| 北京大学   | 综合类  | 北京   | 本科一批   |
| 清华大学   | 综合类  | 北京   | 本科一批   |
| 浙江大学   | 综合类  | 浙江   | 本科一批   |
| 复旦大学   | 综合类  | 上海   | 本科一批   |
| 中国人民大学 | 综合类  | 北京   | 本科一批   |
| 上海交通大学 | 综合类  | 上海   | 本科一批   |
| 武汉大学   | 综合类  | 湖北   | 本科一批   |
| 南京大学   | 综合类  | 江苏   | 本科一批   |
| 中山大学   | 综合类  | 广东   | 本科一批   |
| 北京理工大学 | 理工类  | 北京   | 本科一批   |

>>> print(tabulate(data, headers=hdls, tablefmt="jira"))

|| 学校     || 类别   || 地区   || 招生批次   ||
| 北京大学   | 综合类  | 北京   | 本科一批   |
| 清华大学   | 综合类  | 北京   | 本科一批   |
| 浙江大学   | 综合类  | 浙江   | 本科一批   |
| 复旦大学   | 综合类  | 上海   | 本科一批   |
| 中国人民大学 | 综合类  | 北京   | 本科一批   |
| 上海交通大学 | 综合类  | 上海   | 本科一批   |
| 武汉大学   | 综合类  | 湖北   | 本科一批   |
| 南京大学   | 综合类  | 江苏   | 本科一批   |
| 中山大学   | 综合类  | 广东   | 本科一批   |
| 北京理工大学 | 理工类  | 北京   | 本科一批   |

>>> print(tabulate(data, headers=hdls, tablefmt="presto"))

 学校     | 类别   | 地区   | 招生批次
--------+------+------+--------
 北京大学   | 综合类  | 北京   | 本科一批
 清华大学   | 综合类  | 北京   | 本科一批
 浙江大学   | 综合类  | 浙江   | 本科一批
 复旦大学   | 综合类  | 上海   | 本科一批
 中国人民大学 | 综合类  | 北京   | 本科一批
 上海交通大学 | 综合类  | 上海   | 本科一批
 武汉大学   | 综合类  | 湖北   | 本科一批
 南京大学   | 综合类  | 江苏   | 本科一批
 中山大学   | 综合类  | 广东   | 本科一批
 北京理工大学 | 理工类  | 北京   | 本科一批

>>> print(tabulate(data, headers=hdls, tablefmt="psql"))

+--------+------+------+--------+
| 学校     | 类别   | 地区   | 招生批次   |
|--------+------+------+--------|
| 北京大学   | 综合类  | 北京   | 本科一批   |
| 清华大学   | 综合类  | 北京   | 本科一批   |
| 浙江大学   | 综合类  | 浙江   | 本科一批   |
| 复旦大学   | 综合类  | 上海   | 本科一批   |
| 中国人民大学 | 综合类  | 北京   | 本科一批   |
| 上海交通大学 | 综合类  | 上海   | 本科一批   |
| 武汉大学   | 综合类  | 湖北   | 本科一批   |
| 南京大学   | 综合类  | 江苏   | 本科一批   |
| 中山大学   | 综合类  | 广东   | 本科一批   |
| 北京理工大学 | 理工类  | 北京   | 本科一批   |
+--------+------+------+--------+

>>> print(tabulate(data, headers=hdls, tablefmt="rst"))

======  ====  ====  ======
学校      类别    地区    招生批次
======  ====  ====  ======
北京大学    综合类   北京    本科一批
清华大学    综合类   北京    本科一批
浙江大学    综合类   浙江    本科一批
复旦大学    综合类   上海    本科一批
中国人民大学  综合类   北京    本科一批
上海交通大学  综合类   上海    本科一批
武汉大学    综合类   湖北    本科一批
南京大学    综合类   江苏    本科一批
中山大学    综合类   广东    本科一批
北京理工大学  理工类   北京    本科一批
======  ====  ====  ======

>>> print(tabulate(data, headers=hdls, tablefmt="mediawiki"))

{| class="wikitable" style="text-align: left;"
|+ <!-- caption -->
|-
! 学校     !! 类别   !! 地区   !! 招生批次
|-
| 北京大学   || 综合类  || 北京   || 本科一批
|-
| 清华大学   || 综合类  || 北京   || 本科一批
|-
| 浙江大学   || 综合类  || 浙江   || 本科一批
|-
| 复旦大学   || 综合类  || 上海   || 本科一批
|-
| 中国人民大学 || 综合类  || 北京   || 本科一批
|-
| 上海交通大学 || 综合类  || 上海   || 本科一批
|-
| 武汉大学   || 综合类  || 湖北   || 本科一批
|-
| 南京大学   || 综合类  || 江苏   || 本科一批
|-
| 中山大学   || 综合类  || 广东   || 本科一批
|-
| 北京理工大学 || 理工类  || 北京   || 本科一批
|}

>>> print(tabulate(data, headers=hdls, tablefmt="moinmoin"))

|| ''' 学校     ''' || ''' 类别   ''' || ''' 地区   ''' || ''' 招生批次   ''' ||
||  北京大学    ||  综合类   ||  北京    ||  本科一批    ||
||  清华大学    ||  综合类   ||  北京    ||  本科一批    ||
||  浙江大学    ||  综合类   ||  浙江    ||  本科一批    ||
||  复旦大学    ||  综合类   ||  上海    ||  本科一批    ||
||  中国人民大学  ||  综合类   ||  北京    ||  本科一批    ||
||  上海交通大学  ||  综合类   ||  上海    ||  本科一批    ||
||  武汉大学    ||  综合类   ||  湖北    ||  本科一批    ||
||  南京大学    ||  综合类   ||  江苏    ||  本科一批    ||
||  中山大学    ||  综合类   ||  广东    ||  本科一批    ||
||  北京理工大学  ||  理工类   ||  北京    ||  本科一批    ||

>>> print(tabulate(data, headers=hdls, tablefmt="youtrack"))

||  学校      ||  类别    ||  地区    ||  招生批次    ||
|  北京大学    |  综合类   |  北京    |  本科一批    |
|  清华大学    |  综合类   |  北京    |  本科一批    |
|  浙江大学    |  综合类   |  浙江    |  本科一批    |
|  复旦大学    |  综合类   |  上海    |  本科一批    |
|  中国人民大学  |  综合类   |  北京    |  本科一批    |
|  上海交通大学  |  综合类   |  上海    |  本科一批    |
|  武汉大学    |  综合类   |  湖北    |  本科一批    |
|  南京大学    |  综合类   |  江苏    |  本科一批    |
|  中山大学    |  综合类   |  广东    |  本科一批    |
|  北京理工大学  |  理工类   |  北京    |  本科一批    |

>>> print(tabulate(data, headers=hdls, tablefmt="html"))

<table>
<thead>
<tr><th>学校    </th><th>类别  </th><th>地区  </th><th>招生批次  </th></tr>
</thead>
<tbody>
<tr><td>北京大学  </td><td>综合类 </td><td>北京  </td><td>本科一批  </td></tr>
<tr><td>清华大学  </td><td>综合类 </td><td>北京  </td><td>本科一批  </td></tr>
<tr><td>浙江大学  </td><td>综合类 </td><td>浙江  </td><td>本科一批  </td></tr>
<tr><td>复旦大学  </td><td>综合类 </td><td>上海  </td><td>本科一批  </td></tr>
<tr><td>中国人民大学</td><td>综合类 </td><td>北京  </td><td>本科一批  </td></tr>
<tr><td>上海交通大学</td><td>综合类 </td><td>上海  </td><td>本科一批  </td></tr>
<tr><td>武汉大学  </td><td>综合类 </td><td>湖北  </td><td>本科一批  </td></tr>
<tr><td>南京大学  </td><td>综合类 </td><td>江苏  </td><td>本科一批  </td></tr>
<tr><td>中山大学  </td><td>综合类 </td><td>广东  </td><td>本科一批  </td></tr>
<tr><td>北京理工大学</td><td>理工类 </td><td>北京  </td><td>本科一批  </td></tr>
</tbody>
</table>

>>> print(tabulate(data, headers=hdls, tablefmt="latex"))

\begin{tabular}{llll}
\hline
 学校     & 类别   & 地区   & 招生批次   \\
\hline
 北京大学   & 综合类  & 北京   & 本科一批   \\
 清华大学   & 综合类  & 北京   & 本科一批   \\
 浙江大学   & 综合类  & 浙江   & 本科一批   \\
 复旦大学   & 综合类  & 上海   & 本科一批   \\
 中国人民大学 & 综合类  & 北京   & 本科一批   \\
 上海交通大学 & 综合类  & 上海   & 本科一批   \\
 武汉大学   & 综合类  & 湖北   & 本科一批   \\
 南京大学   & 综合类  & 江苏   & 本科一批   \\
 中山大学   & 综合类  & 广东   & 本科一批   \\
 北京理工大学 & 理工类  & 北京   & 本科一批   \\
\hline
\end{tabular}

>>> print(tabulate(data, headers=hdls, tablefmt="latex_raw"))

\begin{tabular}{llll}
\hline
 学校     & 类别   & 地区   & 招生批次   \\
\hline
 北京大学   & 综合类  & 北京   & 本科一批   \\
 清华大学   & 综合类  & 北京   & 本科一批   \\
 浙江大学   & 综合类  & 浙江   & 本科一批   \\
 复旦大学   & 综合类  & 上海   & 本科一批   \\
 中国人民大学 & 综合类  & 北京   & 本科一批   \\
 上海交通大学 & 综合类  & 上海   & 本科一批   \\
 武汉大学   & 综合类  & 湖北   & 本科一批   \\
 南京大学   & 综合类  & 江苏   & 本科一批   \\
 中山大学   & 综合类  & 广东   & 本科一批   \\
 北京理工大学 & 理工类  & 北京   & 本科一批   \\
\hline
\end{tabular}

>>> print(tabulate(data, headers=hdls, tablefmt="latex_booktabs"))

\begin{tabular}{llll}
\toprule
 学校     & 类别   & 地区   & 招生批次   \\
\midrule
 北京大学   & 综合类  & 北京   & 本科一批   \\
 清华大学   & 综合类  & 北京   & 本科一批   \\
 浙江大学   & 综合类  & 浙江   & 本科一批   \\
 复旦大学   & 综合类  & 上海   & 本科一批   \\
 中国人民大学 & 综合类  & 北京   & 本科一批   \\
 上海交通大学 & 综合类  & 上海   & 本科一批   \\
 武汉大学   & 综合类  & 湖北   & 本科一批   \\
 南京大学   & 综合类  & 江苏   & 本科一批   \\
 中山大学   & 综合类  & 广东   & 本科一批   \\
 北京理工大学 & 理工类  & 北京   & 本科一批   \\
\bottomrule
\end{tabular}

>>> print(tabulate(data, headers=hdls, tablefmt="textile"))

|_.  学校     |_. 类别   |_. 地区   |_. 招生批次   |
|<. 北京大学    |<. 综合类  |<. 北京   |<. 本科一批   |
|<. 清华大学    |<. 综合类  |<. 北京   |<. 本科一批   |
|<. 浙江大学    |<. 综合类  |<. 浙江   |<. 本科一批   |
|<. 复旦大学    |<. 综合类  |<. 上海   |<. 本科一批   |
|<. 中国人民大学  |<. 综合类  |<. 北京   |<. 本科一批   |
|<. 上海交通大学  |<. 综合类  |<. 上海   |<. 本科一批   |
|<. 武汉大学    |<. 综合类  |<. 湖北   |<. 本科一批   |
|<. 南京大学    |<. 综合类  |<. 江苏   |<. 本科一批   |
|<. 中山大学    |<. 综合类  |<. 广东   |<. 本科一批   |
|<. 北京理工大学  |<. 理工类  |<. 北京   |<. 本科一批   |

>>> td = ((1, 123456, 123.456), (2, 234, 234.5), (3, 3, 3.4))

>>> print(tabulate(td))

-  ------  -------
1  123456  123.456
2     234  234.5
3       3    3.4
-  ------  -------

(注意：此时浮点数根据小数点位置对齐)

>>> print(tabulate(td, numalign="center"))

-  ------  -------
1  123456  123.456
2   234     234.5
3    3       3.4
-  ------  -------

>>> print(tabulate(td, numalign="left"))

-  ------  -------
1  123456  123.456
2  234     234.5
3  3       3.4
-  ------  -------

>>> print(tabulate(td, numalign="right"))

-  ------  -------
1  123456  123.456
2     234    234.5
3       3      3.4
-  ------  -------

>>> import os

>>> os.chdir("D:/")

>>> import qrcode

>>> img = qrcode.make("https://python123.io")

>>> img.save("python123.png")

(请在D盘下查看生成的图片文件)

>>> tg = qrcode.make("Python语言开创事业")

>>> tg.save("python.png")

(请在D盘下查看生成的图片文件)

>>> tg = qrcode.make(tabulate(data, headers=hdls, tablefmt="html"))

>>> tg.save("datahtml.png")

(请在D盘下查看生成的图片文件)

>>> tg = qrcode.make(tabulate(td))

>>> tg.save("data.png")

(请在D盘下查看生成的图片文件)
小测验
请将如下代码粘贴至"提交代码"页面，"保存并提交评判"后查看结果。注意，此时代码不是交互模式，而是文件模式。 

from tabulate import tabulate
d = eval(input())
s = tabulate(d, tablefmt = "jira")
t = s.replace(" | ", " & ")
print(t)

习题讲解
【代码分析】

from tabulate import tabulate
d = eval(input())
s = tabulate(d, tablefmt = "jira")
t = s.replace(" | ", " & ")
print(t)
此代码训练了tabulate库的基本使用，通过字符串的replace()方法可以更改tabulate的输出风格。

常用第三方库之pipenv小练习
描述
这是一个关于"常用第三方库之pipenv"的小练习，覆盖pipenv库的基本操作，包含两部分内容：跟随练习 和 小测验。

在"跟随练习"环节，请使用Windows命令行工具，逐一输入以下语句，观察并比较输出结果。

在"小测验"环节，请在本题目对应的"提交代码"页面按要求输入代码，"保存并提交评判"后查看结果。

跟随练习
 请使用Windows命令行工具，这里建议采用Cmder，下载地址：http://cmder.net/，（特征是 λ 提示符），按顺序逐一输入以下语句（共20个）：

λ> D:\

λ> mkdir pEnv

λ> cd pEnv

λ> pipenv -h 

Usage: pipenv [OPTIONS] COMMAND [ARGS]...

Options:
  --where             Output project home information.
  --venv              Output virtualenv information.
  --py                Output Python interpreter information.
  --envs              Output Environment Variable options.
  --rm                Remove the virtualenv.
(略)

λ> pipenv --venv

No virtualenv has been created for this project yet!

λ> pipenv --three

Creating a virtualenv for this project...
Pipfile: D:\pEnv\Pipfile
(略)

λ> pipenv shell

Launching subshell in virtual environment…
Microsoft Windows [版本 10.0.16299.15]
(c) 2017 Microsoft Corporation。保留所有权利。

(pEnv-g0vMOMWU) D:\pEnv>

(略)

(pEnv-g0vMOMWU) > pipenv install jieba

(略)

(pEnv-g0vMOMWU) > pipenv install wordcloud

(略)

(pEnv-g0vMOMWU) > pipenv install tabulate

(略)

(pEnv-g0vMOMWU) > pipenv graph

(略)

(pEnv-g0vMOMWU) > pipenv -h

(略)

(pEnv-g0vMOMWU) > exit

(略)

λ> pipenv --venv

C:\Users\Tian Song\.virtualenvs\pEnv-g0vMOMWU

λ> cd D:\

λ> mkdir p2Env

λ> cd p2Env

λ> pipenv --python 3.6

Creating a virtualenv for this project...
Pipfile: D:\p2Env\Pipfile
(略)

λ> pipenv shell

(略)
小测验
请将如下代码粘贴至"提交代码"页面，"保存并提交评判"后查看结果。注意，此时代码不是交互模式，而是文件模式。 

s = '''
Usage: pipenv [OPTIONS] COMMAND [ARGS]...
Commands:
  check      Checks for security vulnerabilities and against PEP 508 markers
             provided in Pipfile.
  clean      Uninstalls all packages not specified in Pipfile.lock.
  graph      Displays currently-installed dependency graph information.
  install    Installs provided packages and adds them to Pipfile, or (if none
             is given), installs all packages.
  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the virtualenv.
  shell      Spawns a shell within the virtualenv.
  sync       Installs all packages specified in Pipfile.lock.
  uninstall  Un-installs a provided package and removes it from Pipfile.
  update     Runs lock, then sync.
'''
cmd = input()
if cmd == "pipenv":
   print(s)

习题讲解
【代码分析】

s = '''
Usage: pipenv [OPTIONS] COMMAND [ARGS]...
Commands:
  check      Checks for security vulnerabilities and against PEP 508 markers
             provided in Pipfile.
  clean      Uninstalls all packages not specified in Pipfile.lock.
  graph      Displays currently-installed dependency graph information.
  install    Installs provided packages and adds them to Pipfile, or (if none
             is given), installs all packages.
  lock       Generates Pipfile.lock.
  open       View a given module in your editor.
  run        Spawns a command installed into the virtualenv.
  shell      Spawns a shell within the virtualenv.
  sync       Installs all packages specified in Pipfile.lock.
  uninstall  Un-installs a provided package and removes it from Pipfile.
  update     Runs lock, then sync.
'''
cmd = input()
if cmd == "pipenv":
   print(s)
此代码希望大家能够对pipenv二级指令所较为全面了解。

中文词语逆序
描述
获得用户输出的中文字符串，按照词语进行逆序输出。

输入格式
中文字符串

输出格式
中文字符串 

输入输出示例
 

 	输入	输出
示例 1	
这是一个输入输出示例
hello Alice
hello Bob

习题讲解
【参考代码】

import jieba
s = input()
ls = jieba.lcut(s)
print("".join(ls[::-1]))

《白鹿原》之最长单词
描述
附件是《白鹿原》原著内容，请读入内容，分词后输出最长单词。

如果存在多个单词长度一致，请输出按照Unicode排序后最大的单词。

输入格式
文件

输出格式
字符串

输入输出示例
仅提供一个输出示范样例。

 	输入	输出
示例 1	
无
白鹿原
 

附件
序号
名称 程序内使用说明
1
白鹿原.txt

习题讲解
【参考代码】

import jieba
f = open("白鹿原.txt")
ls = jieba.lcut(f.read())
A = set(ls)
maxw = ""
for w in A:
    if len(w) > len(maxw):
        maxw = w
    if len(w) == len(maxw) and w > maxw:
        maxw = w
print(maxw)
f.close()
分词后产生列表，转换为集合进行去重。字符串之间存在顺序，可以直接使用>=<等符号比较。

《白鹿原》之最多单词
描述
附件是《白鹿原》原著内容，请读入内容，分词后输出长度大于2且最多的单词。

如果存在多个单词出现频率一致，请输出按照Unicode排序后最大的单词。

输入格式
文件

输出格式
字符串

输入输出示例
仅提供一个输出示范样例。

 	输入	输出
示例 1	
无
白鹿原
 

附件
序号
名称 程序内使用说明
1
白鹿原.txt

习题讲解
【参考代码】

import jieba
f = open("白鹿原.txt")
ls = jieba.lcut(f.read())
d = {}
for w in ls:
    d[w] = d.get(w, 0) + 1
maxc = 0
maxw = ""
for k in d:
    if d[k] > maxc and len(k) > 2:
        maxc = d[k]
        maxw = k
    if d[k] == maxc and len(k) > 2 and k > maxw:
        maxw = k
print(maxw)
f.close()
使用字典d形成 单词:次数 的键值对，遍历获取其中最大值。

WordCloud词云生成 I
描述
wordcloud是生成词云的Python第三方库，也是Python优秀的计算生态之一。

下面是一段生成词云的代码，但这段代码并不能如期产生词云。请在不改变代码行数的情况下，修改代码，达到生成词云的目的。

import wordcloud
c = wordcloud.WordCloud()
c.generate("Python Java Python JavaScript Python Go Python Ruby Python Lua")
c.save_file("outfile.png")
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

习题讲解
【参考代码】

 能够正确运行的完整代码如下：

import wordcloud
c = wordcloud.WordCloud()
c.generate("Python Java Python JavaScript Python Go Python Ruby Python Lua")
c.to_file("outfile.png")
其中，生成图片文件的方法是to_file()，该题目答案如下：

print('c.to_file("output.file")')

二维数据表格输出 I
描述
tabulate能够对二维数据进行表格输出，是Python优秀的第三方计算生态。

参考编程模板中给定的数据和代码，编写程序，能够输出如下风格效果的表格数据。



输入格式
参考编程模板中部分代码

输出格式
参考上图中效果

习题讲解
【参考代码】

from tabulate import tabulate
data = [ ["北京理工大学", "985", 2000], \
         ["清华大学", "985", 3000], \
         ["大连理工大学", "985", 4000], \
         ["深圳大学", "211", 2000], \
         ["沈阳大学", "省本", 2000], \
    ]
print(tabulate(data, tablefmt="grid"))
对各种表格风格进行尝试。



