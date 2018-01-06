a =  1234#帐号
p = 123#密码
c = int(input("请输入帐号"))
d = int(input("请输入密码"))
m = 1
n = 0
if c == a and d == p:
	print("登录成功")
	v = input("请输入0,鲁班大师 1,陈要紧 2,小乔")
	if v == "0":
		print("鲁班大师")
	elif v == "1":
		print("陈要紧")
	elif v == "2":
		print("小乔")
	n = n+1
if c !=a and d !=p:
	while m <= 3 and n == 0:
	c = int(input("请输入帐号"))
	d = int(input("请输入密码"))
	m +=1
	
if m == 3:
	print("你在干嘛")
