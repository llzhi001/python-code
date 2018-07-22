#1.利用递归方法求5！

def digui(j):
    sum_value = 0
    if j == 0:
        sum_value = 1
    else:
        sum_value = j * digui(j-1)
    return sum_value
for i in range(10):
    print('%d!=%d' % (i,digui(i)))

#2.利用递归函数调用方法，将所输入的5个字符，以相反顺序打印出来

def output(s,l):
    if l == 0:
        return
    print(s[l-1])
    output(s,l-1)
s = input('输入一个字符串：')
l = len(s)
output(s,l)

#3.按逗号分隔列表

l = ['a','b','c',123]
s = ','.join(str(n) for n in l)
print(s)

#4.将一个数组逆序输出

a = [5,1,8,6,7,9]
n = len(a)
print(a)
for i in range(int(len(a)/2)):
    a[i],a[n-1-i] = a[n-1-i],a[i]
print(a)

#5.两个3行3列的矩阵，实现其对应位置的数据相加，并返回一个新矩阵

x = [[1,2,3],[4,5,6],[7,8,9]]
y = [[10, 2, 3], [4, 50, 6], [7, 8, 90]]
Z = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

for i in range(3):
    for j in range(3):
        Z[i][j] = x[i][j] + y[i][j]
for z in Z:
    print(z)

#6.匿名函数求和

sum_value = lambda x,y:x+y
print(sum_value(1,2))

#7.查找字符串的位置

s1 = 'asdffgdh'
s2 = 'ffg'
print(s1.find(s2))

#8.在字典中找到年龄最大的人，并输出

people = {'laowang':40,'lisi':30,'zhangsan':45}
m = 'lisi'
for key in people.keys:
    if people[m] < people[key]:
        m = key    
print(m,people[m])

#9.列表转换为字典

k = ['zhang','san']
v = [123,456]
print(dict([k,v]))

#10.从键盘输入一个字符串，将小写字母全部转换成大写字母，然后输出到一个磁盘文件“test”中保存

f = open('test.txt', 'w')
s = input('输入一个字符串')
s = s.upper()
f.write(s)
f.close()

f = open('test.txt', 'r')
print(f.read())
f.close


