def minus(a):
    if str(a).count('.'):  # 判断小数点是不是大于1
        a = float(a)
        a = a-1
        return a
    elif str(a).isdigit():
        a = int(a)
        a = a-1
        return a
    else:
        return "参数格式错误"

if __name__ == "__main__":
    print("这是一个Python小模块")

