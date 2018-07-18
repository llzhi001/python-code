import requests
import time

# 登录验证地址
check_url = 'http://www.finndy.com/midycp.php?action=profile'

# 记录程序运行时的时间
fp = open('./auto_signon_finndy.log','a')
ISOTIMEFORMAT='%Y-%m-%d %X'
curtime = time.strftime( ISOTIMEFORMAT, time.localtime( time.time() ) )
print('at %s'%curtime)
fp.write('at %s\n'%curtime)

# 准备cookie
print('准备cookie中……')
fp.write('准备cookie中……\n')
cookie_str = 'finndy_seccode=953c77cAmKf0J2QKiL9nFG1k52CCvT7mUh24TFsSeROw; finndy_auth=6777bMXE5Mi8PDheZpxEFnJAHl%2B5vD75pQKC0WOchBdxlsfZPTdm1U1g5YKQJPcxG00cRaX0laIxme9wcpGhD2fnFak; finndy_loginuser=18521099743; Hm_lvt_fafaa7b25f2d04f0c302463ddf631057=1520994342,1520994761,1520994876; finndy__refer=http%3A%2F%2Fwww.finndy.com%2Frobot.php%3Frobotid%3D273466; Hm_lpvt_fafaa7b25f2d04f0c302463ddf631057=1520997590; finndy_verifyid=1783f815a0e1487696d827d0a745848a; _pk_ref.1.1450=%5B%22%22%2C%22%22%2C1522375822%2C%22https%3A%2F%2Fwww.baidu.com%2Fbaidu.php%3Fsc.060000jZYuibWkd0MJg3hbRAgoefxJNoE7ylMfdaqWOnZHa8QXq_LwQnMw-dPQBj-V6qQtPWNcYCtYqxRNwDOrTMYRgSYNkwgwUZxRMFK9a0aXc-ni4LktSvKIk3wmXq9SqKgZC9IPVvs3FcB1fGMDj2vKAblgrN224U2-o_vEequRZK36.Db_jyS22efBj81jfXlQrMnSF2hGv-5QWdQjPakg8LX57f0.U1Yk0ZDq8Oa1VTvL__htotUL0ZKGm1Ys0Zfq8Oa1VTvL__htotUL0A-V5HczPfKM5yF-TZns0ZNG5yF9pywd0ZKGujYz0APGujYYnjm0UgfqnH0kPdtknjD4g1csPWFxn1msnfKopHYs0ZFY5HmdP0K-pyfqnHf1P-tznH03n-tkrjRvn7tkP10snNtznjm4PdtznW0LPfKBpHYznjf0UynqP1cLnH6dPjfLg1TzP1TknW6dP7tzrjn4P1mzP164g100TgKGujYs0Z7Wpyfqn0KzuLw9u1Ys0A7B5HKxn0K-ThTqn0KsTjYznWc4njT3P1fY0A4vTjYsQW0snj0snj0s0AdYTjYs0AwbUL0qn0KzpWYs0Aw-IWdsmsKhIjYs0ZKC5H00ULnqn0KBI1Ykn0K8IjYs0ZPl5fKYIgnqPWcLnHRYnj0vPW0kPjfYrHDsnfKzug7Y5HDdnW04rHf1n1f3rHR0Tv-b5H-BPAfLnjmdnj0snjmYmyn0mLPV5H0YwDDvf1IDnWn3wH6dwHD0mynqnfKsUWYs0Z7VIjYs0Z7VT1Ys0ZGY5H00UyPxuMFEUHYsg1Kxn7ts0Aw9UMNBuNqsUA78pyw15HKxn7tsg100TA7Ygvu_myTqn0Kbmv-b5H00ugwGujYVnfK9TLKWm1Ys0ZNspy4Wm1Ys0Z7VuWYkP6KhmLNY5H00uMGC5H00uh7Y5H00XMK_Ignqn0K9uAu_myTqnfK_uhnqn0KWThnqnWTkrHf%26ck%3D3470%22%5D; _pk_ses.1.1450=*; _pk_id.1.1450=b90eaefdfd783242.1520994342.3.1522376466.1522375822.'
cookie = {}
for line in cookie_str.split(';'):
    name,value=line.strip().split('=',1)
    cookie[name]=value
print(cookie)
fp.write('%s\n'%cookie)

# 使用cookie访问网站
print('签到中……')
fp.write('签到中……\n')
res = requests.get(check_url,cookies=cookie)
print(res)
fp.write('%s\n\n'%res)