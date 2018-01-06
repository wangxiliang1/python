x = 0
a = 123
b = 123
money = 1000
n = 0
for i in range(1,4):
		c = int(input("请输入帐号"))
		d = int(input("请输入密码"))
		if c == a and d == b:
			print("登录成功")
			e = input("存钱请按2,取钱请按1")
			if e == "2":
				s = int(input("请输入所要存的金额"))
				n = money+s
				print("你原有的金额为:%d 存入了:%d 现有金额:%d"%(money,s,n))
			elif e == "1":
				v = int(input("请输入你所要取的金额"))
				if v <= money:
					x = money-v
					print("你原有金额为:%d 本次索取:%d 剩余:%d"%(money,v,x))
				else:
					print("你的余额不足")
			break	
		else:
			print("你是傻子吧，自己的帐号密码都不知道")
