count = 0
a = 0#偶数
b = 0#奇数
while count < 10:
	if count%2 == 0:
		a += count
	if count%2 != 0:
		b += count
	count += 1
print("偶数和是%d" % a)
print("奇数和是%d" % b)
