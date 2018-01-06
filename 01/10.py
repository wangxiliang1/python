oushu = 0
jishu = 0
for i in range(1,100):
	if i%2 == 0:
		oushu += i
		print(oushu)
	elif i%2 !=0:
		jishu += i
		print(jishu)
	print(jishu-oushu)
