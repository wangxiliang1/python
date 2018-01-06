a = float(input("请输入你的身高m"))
b = int(input("请输入你的体重kg"))
c = b/a**2
print(c)
if c < 18.5:
	print("体重过轻")
elif c > 18.5 and c <= 25:
	print("过重")
elif c > 25 and c <= 28:
	print("肥胖")

