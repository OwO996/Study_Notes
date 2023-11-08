# Python 的 Bool 类型

Bool 类型，其实就是特殊的整数类型。

> 对于错、0和1、正与反，都是传统意义上的布尔类型。
>
> 但在Python语言中，布尔类型只有两个值，True与False。请注意，是英文单> 词的对与错，并且首字母要大写，不能其它花式变型。
>
> 所有计算结果，或者调用返回值是True或者False的过程都可以称为布尔运
> 算，例如比较运算。布尔值通常用来判断条件是否成立。
>
> 空值不是布尔类型，严格的来说放在这里是不合适的，只不过和布尔关系比
> 较紧密。
>
> 空值是Python里一个特殊的值，用None表示（首字母大写）。None不能理
> 解为0，因为0是整数类型，而None是一个特殊的值。None也不是布尔类
> 型，而是NoneType。
>
> 引用自 [刘江的博客教程][0]{:target="_blank"}。

## 会被返回 False 的情况

1. 数字只有等值于 0 的结果才会被 bool() 返回 False；
2. 字符串只有是空的时候才会被 bool() 返回 False，一个空格也会被返回 True；

> 会被返回 False 的对象：
> 空的序列和集合：'', (), [], {}, set(), range(0)；
> 值为 0 的数字类型：0, 0.0, 0j, Decimal(0), Fraction(0, 1)；
> 定义为 False 的对象：None 和 False。

## 逻辑运算符（bool 运算符）

Python 总共有三个运算符号：and、or、not。以下为这三种运算符的含义的示意图。

![这三种运算符的含义](http://tg.owo233.eu.org:8080/246/photo-2023-11-08_16-35-30.jpg?hash=00ad24)

> Python 中的任何对象都能直接进行真值测试（测试该对象的 bool 类型值为 
> True 或者 False）用于 if 或者 while 语句的条件判断，也可以作为 bool 逻辑
> 运算符的操作数。

### Python 的逻辑运算符的特性

1. Python 中的 and 会计算两侧的表达式，如果两侧表达式的值均为真的话，则会输出后一个值，如果有一个值是假的，则会输出假的值；
2. Python 中的 or 运算符是短路运算符，他会先计算第一个表达式的值，第一个表达式的值如果不为 False，则第一个表达式的值委决定整个表达式的值，反之，则会计算第二个表达式的值来决定整个表达式的值，因此，输入字符串或者数字，如果第一个值或者数字不为 False，会直接输出第一个数字或者文本；
3. Python 是支持链式比较的，链式比较能简化代码；
4. Python 中，语句的判断条件的真值测试是会自动进行的，不使用 bool() 函数也没有任何问题；
5. 在 Python 中，True 等值于 1，False 等值于 0；

## 拓展：学习 fractions 模块

在 Python 中，fractions 是一个模块，用于表示和处理分数。它提供了 Fraction 类，该类表示一个有理数。Fraction 类继承自抽象基类 numbers.Rational，并实现了该类的所有方法和操作。

Fraction 实例可以由一对整数、一个分数，或者一个字符串构建而成。例如，以下代码创建了两个 Fraction 实例：

```Python
>>> from fractions import Fraction
>>> f1 = Fraction(1, 2)
>>> f2 = Fraction('1/2')
```

f1 和 f2 的值都为 1/2。

Fraction 实例支持基本的算术运算，包括加、减、乘、除、取模、幂运算和比较运算。例如，以下代码使用了 Fraction 实例的算术运算：

```Python
>>> f3 = f1 + f2
>>> f4 = f1 - f2
>>> f5 = f1 * f2
>>> f6 = f1 / f2
>>> f7 = f1 % f2
>>> f8 = f1 ** 2
>>> f9 = f1 == f2
>>> f10 = f1 < f2

>>> print(f3)
1/1
>>> print(f4)
0
>>> print(f5)
1/4
>>> print(f6)
2
>>> print(f7)
0
>>> print(f8)
1/4
>>> print(f9)
True
>>> print(f10)
False
```

Fraction 实例还支持一些其他操作，例如将分数转换为字符串、将分数转换为浮点数、计算分数的约分等。例如，以下代码使用了 Fraction 实例的其他操作：

```Python
>>> str(f1)
'1/2'
>>> float(f1)
0.5
>>> f1.limit_denominator(100)
Fraction(50, 100)
```

并且 Fraction 实例还能 **直接将输入的分数约分**，例如：

```Python
>>> from fractions import Fraction
>>> print(Fraction('1708227363155544/4636617128565048'))
7/19
```

总而言之，fractions 模块提供了一个强大的工具，用于处理分数。

## 实例

### 输入一个年份，然后程序输出是否为闰年或者世纪闰年。

#### 思路

1. 公历年份是 4 的倍数，并且不能是 100 的倍数，为普通闰年；
2. 公历年份是整百数的，必须是 400 的倍数，才是世纪闰年；
3. 所以普通闰年的检测条件是：“not x % 4 and x % 100”，x 除上 4 没有余数，返回 0，not 0 则等于 True 也就是 1，反之，则会的到 0，然后同时 x 除以 100 有余数则会返回非 0 数，无余数则会返回 0，解决检测普通闰年的条件；
4. 世纪闰年的检测条件是：“not x % 400”，因为只要能被 400 除尽，则一定能被 100 整除；
5. 所以编写本程序总共需要两个变量，用于确认用户的输入以及完成对闰年的确认，两个变量设置为：x、z。
6. 因为普通闰年不可能和世纪闰年是同一年，所以只需要使用 if elif ... else 结构即可。

#### 程序本体

```Python
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
```

[0]: https://www.liujiangblog.com/course/python/18