i = 0
x = ''
z = ''

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

x = int(x)
z = 0

if x >= 0:
    while i <= x:
        if i % 2 == 0:
            z = i + z
        i = i + 1
else:
    while i >= x:
        if i % 2 == 0:
            z = i + z
        i = i - 1

print(z)