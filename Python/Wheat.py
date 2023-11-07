i = 1
y = 1
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
# 抽象题目即可得出，输入一个整数，然后从一个值 i 记录已经循环的次数，使用 x 来记录需要
# 循环的次数，然后循环从 1 开始每次进入下个循环都乘二，并且将每次循乘二后的值作为 y，
# 将每次循环的 y 相加得到值 z，这样可以做到让用户输入需要循环的次数。
x = int(x)
z = 0

while i <= x:
    z = y + z
    y = y * 2
    i = i + 1

print(z)