a = int(input("请输入一个年份"))
if (a%4 == 0 and a%100 !=0) or (a%400 == 0):
	print("这是润年")
else:
	print("这是平年")
