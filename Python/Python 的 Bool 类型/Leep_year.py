# 因为 input() 语句只能导入字符串，所以刚开始定义的时候定义为字符串，后续转换成数字
# 即可。
x = ''
z = ''
# 之前用来确认用户输入的模板。
while True:
    while True:
        x = input("请输入一个整数：")
        z = input('请再次输入这个整数：')
        if z == x:
            break
        else:
            print('您的两次输入不一致。')
    z = str(abs(int(x)))
    if z.isdigit():
        break
    else:
        print('您需要输入一个整数。')
# 因为下面的程序只使用了一个变量 x，所以只需要转换 x 的格式即可。
x = int(x)

if not x % 4 and x % 100:
    print('%d 是普通闰年~'% x)
elif not x % 400:
    print('%d 是世纪闰年~'% x)
else:
    print('%d 既不是普通闰年也不是世纪闰年~'% x)