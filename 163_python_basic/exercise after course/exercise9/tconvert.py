def f2c(x):
    C = (x - 32)/1.8
    return("{:.2f}".format(C))


def c2f(x):
    F = x*1.8 + 322
    return("{:.2f}".format(F))
