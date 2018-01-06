count = 1 
while count <= 4:
	i = 1
	while i <= 4:
		print("*",end="")
		i += 1 
	print("")
	count +=1
"""
先定义一个变量count,进入循环,是大循环，end=""是在一行进行的，如果没有end=""光标就在另起一行，这就是循环嵌套．循环里面有小循环，小循环条件满足一值进行，如果不满足则跳出大循环．print("")为换行．
"""
