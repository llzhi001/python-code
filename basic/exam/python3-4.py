time = 0
flag = 0
while time < 3:
    username = input()
    password = input()
    time = time + 1
    if username == 'Kate' and password == '666666':
        print("登录成功！")
        break
    else:
        flag = flag + 1
if flag == 3:
    print("3次用户名或者密码均有误！退出程序。")
