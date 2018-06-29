def kuo(left=0, right=0, s='', res=[]):
    if left == 0 and right == 0:
        res.append(s)
    elif left == right:
        kuo(left-1, right, s + '(', res)
    else:
        if left > 0:
            kuo(left-1, right, s + '(', res)
        kuo(left, right-1, s + ')', res)


res = []
s = ''
num = eval(input())
kuo(num, num, s, res)
print(res)
