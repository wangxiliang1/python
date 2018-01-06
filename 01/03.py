"""
a = 1
while a <= 5:
	b = 1
	while b <= a:
		print("*",end="")
		b+=1
	print("")
	a +=1
a = 4
while a > 0:
	print("*"*a)
	a-=1
"""
"""
for i in range(1,10):
	for a in range(1,i+1):
		print("%d*%d=%d"%(a,i,a*i),end="\t")
	print("")
"""
"""
m = 0
i = 1
while i < 10:
	a = 1
	while a <= i:
		m = a*i
		print("%d*%d=%d"%(a,i,a*i),end="\t")
		a+=1
	print("")
	i+=1 
"""

"""
for i in range(1,1999):#i是计数器,for循环里i自动加1.
	if i%2 == 0:
		print(i)
"""

range = "abcdefghijklmn"
for i in range:
	print(i,end="")
print("")











