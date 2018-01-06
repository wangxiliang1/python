account = "123"
passwd = "123"
money = 1000
a = input("请输入帐号")
b = input("请输入密码")
if a == account and b == passwd:
    c = int(input("登录成功，取钱请按1,存钱请按2:   "))
    if c == 1:
        mymoney = int(input("请输入你取的钱"))
        print("你取了%d的钱　还剩余%d的钱"%(mymoney,money-mymoney))
    elif c == 2:
        cunmoney = int(input('请输入你要存的金额：'))
        print ('你存了%d元，余额为%d元！'%(cunmoney,money+cunmoney))
else:
    print("你输入的账号或密码错误")
