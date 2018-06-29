def grade(a):
    if a >= 90:
        print("输入成绩属于A级别。")
        print("祝贺你通过考试！")
    elif a >= 80:
        print("输入成绩属于B级别。")
        print("祝贺你通过考试！")
    elif a >= 70:
        print("输入成绩属于C级别。")
        print("祝贺你通过考试！")
    elif a >= 60:
        print("输入成绩属于D级别。")
        print("祝贺你通过考试！")
    else:
        print("输入成绩属于E级别。")


a = input()
try:
        b = eval(a)
        if b <= 100 and b >= 0:
            grade(b)
        else:
            raise Exception
except Exception:
    print("输入数据有误！")
finally:
    print("好好学习，天天向上！")
