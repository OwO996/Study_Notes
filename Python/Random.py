# 此程序用来模拟抛硬币。

import random
# 提前声明变量。
i = 0
x = 0
y = 0
z = 0
# 此循环用来判断输入的整数是否一致以及输入的数据是否为整数。
while True:
    while True:
        x = input("请输入一个整数：")
        z = input('请再次输入这个整数：')
        if z == x:
            break
    if x.isdigit():
        break
    else:
        print('您需要输入一个整数。')
# 因为 input 获取的数据为字符串，所以需要重新转换数据为整数。
x = int(x)
z = int(z)
# 模拟抛硬币并且输出结果。
while y < x:
    y = y + 1
    i = random.randint(1, 2)
    if i == 1:
        print("正面\n")
    else:
        print("反面\n")
