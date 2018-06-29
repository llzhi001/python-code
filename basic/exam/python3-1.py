past = 0
now = 1
output = 1
n = eval(input())
if n == 0:
    print("0, 0, 0")
elif n == 1:
    print("0, 1, 1, 2, %d" % (2/3))
else:
    print("0, 1, ", end='')
    s = 1
    d = 2
    while output <= n:
        print("%d, " % output, end='')
        s = s + output
        d = d + 1
        past = now
        now = output
        output = past + now
    print("%d, %d" % (s, s/d))
