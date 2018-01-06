"""
1 = "石头"
2 = "剪刀"
3 = "布"
"""

import random
a = int(input("请输入1,3"))
b = random.randint(1,3)
if (a == 1 and b == 2) or (a == 2 and b == 3) or (a == 3 and b == 1):
    print("我好棒棒啊")
elif a == b:
    print("哇，我们都好棒棒啊")
else:
    print("你好厉害")
