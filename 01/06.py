d = 180
e = 1000000
f = 90
a = float(input("请输入你的身高m"))
b = int(input("请输入你的身价"))
c = int(input("请输入你的颜值分"))
if a > d and b > e and c > f:
	print("高副帅")
elif a < d and b < e and c > f:
	print("还行")
elif a < d and b < e and c < f:
	print("唉穷搓")
