h = float(input("请输入身高(m)"))#如果不加float那么系统默认的是str 
w = float(input("请输入体重(kg)"))
c = w/h**2
print(c)
if c < 18.5:
        print("过轻")
elif c > 18.5 and c < 25:
        print("正常")
elif c > 25 and c < 28:
        print("过重")
elif c > 28 and c < 32:
        print("肥胖")
elif c > 32:
        print("过于肥胖")
else:
        print("凉了")
