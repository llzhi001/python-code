#快乐的数字
def ifHappy(n):
    if n == 1:
        print(True)
    elif 1<n<10:
        print(False)
    else:
        value = str(n)
        num = 0
        for i in range(len(value)):
            num += int(value[i])**2
        ifHappy(num)

N = eval(input())
ifHappy(N)