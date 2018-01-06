lon = float(input("请输入你的身高"))
body = int(input("请输入你的身价"))
face = float(input("请输入你的颜值分数"))
if lon > 180 and body > 1000000 and face > 90:
	print("哇，你是哟个高副帅唉")
elif lon < 180 and body < 1000000 and face > 90:
	print("恩，你只是有点帅而已")
elif lon < 160 and body < 100 and face < 60:
	print("又是一个唉穷搓")
else:
	print("唉，哥哥我对你很失望")
