'''
字符串垂直输出
描述
将输入的字符串垂直输出 

 

输入格式
这是一个字符串

 

输出格式
多行字符串 

 

输入输出示例
 

 	输入	输出
示例 1	
中英文String
中
英
文
S
t
r
i
n
g
'''

a = input()
for i in a:
    print('{}'.format(i),end='\n')
