import random
c = random.randint(1,100)
for i in range(1,10):
	a = int(input("请输入一个数字1,100"))
	if a == c:
		print("猜中")
		break
	elif a > c:
		print("我赢")
	elif a < c:
		print("电脑获胜")
