# import numpy as np

# colors = ['black', 'white']
# sizes = ['S', 'M', 'L']
# # 生成器表达式
# for tshirt in ('%s %s' % (c, s) for c in colors for s in sizes):
#     print(tshirt)
# a = 1
# # 列表推导
# red = [(c, s) for c in colors for s in sizes]
# print(red)
# b = range(10)
# print(type(b))
# print(b)
# a = np.array([1, 1, 1])
# print(a)
# print(a.reshape(1, 3))
# a = np.array([1, 1, 1])[:, np.newaxis]
# a = np.array([1, 1, 1])[np.newaxis, :]
# print(a)
# b = np.arange(12).reshape(3, 4)

# print('*************************')
# print(np.vsplit(b, 3))
# print('*******************************')
# print(np.split(b, 2, 1))  # 横向对等分割，axis=1,按横向分割，axis=0，按纵向分割
# print(np.array_split(b, 3, 1))  # 不对等分割
# print()
# np.random.seed(0)
# a = np.random.random(10)
# print(a)
# print(type(a))


# def reciprocal(values):
#     values_out = np.empty(len(values))  # 要对np数组进行操作先生成数组
#     for i in range(len(values)):
#         values_out[i] = 1/values[i]
#     return values_out


# print(reciprocal(a))
# b = np.random.randint(0, 10, size=10)
# print(reciprocal(b))
# print(b)
# print(2/2)
# print(1.0/2)
# # import os
# # os.system("ping www.baidu.com")
# x = lambda a : a % 2
# print(list(filter(x,range(6))))
# a = ['hello','my','visit']
# b = 'hello'
# print(id(b))
# print(id(b[::-1]))
# a = [0,1,2,3,4,5,6,7,8,9]
# print((a[:6:-1]))
# print(a[:8][2:5][-1:])
# print(range(1,100))
# print(list(range(1,100)[2::3][-5:]))
import dis


def cba(a):
    return a[::-1]


# def abc():
#     a = ['cherry', 'banana']
#     b = sorted(a, key=lambda b: b[::-1])


# print(dis.dis(abc))
a = ['cherry', 'banana', 'green', 'red', 'strawberry']
b = sorted(a, key=lambda word: word[::-1])
print(b)


def fact(n):
    a = 1
    for i in range(n):
        a = a * (i + 1)
    return a


def fact1(n):
    return 1 if n < 2 else n * fact1(n - 1)


def fact2(n):
    a = 1
    if n < 0:
        print('负数不能参与阶乘！')
    else:
        for i in range(1, n + 1):
            a = a * (i)
    return a


# def fact2(n):
#     b = 1
#     for i in range(n):


from functools import reduce
from operator import add

s = list(map(fact2, range(9)))
print(s)
s = list(map(fact1, range(6)))
print(s)
s = filter(lambda s: s % 2, range(6))
s = reduce(add, range(100))
print(s)
print(sum(range(100)))
print(list(range(0)))

a = 1
for i in range(1, 1):
    a = a * (i + 1)
    print(i, 'sdfgfafhsapf')
print(a, 'sdhfsda')
from functools import reduce
from operator import mul
from operator import itemgetter


def fact11(n):
    if n == 0:
        return 1
    else:
        return reduce(lambda a, b: a * b, range(1, n + 1))


print(list(map(fact11,range(6))))
a = lambda word: word[::-1]
print(a(['abc', 'uvw', 'xyz']))
b = itemgetter(1,0)
c = ['123','3','23']
print(type(b(c)))


