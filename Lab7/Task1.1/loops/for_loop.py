# 3.
# A.py
# a = int(input())
# b = int(input()) + 1
# [print(i, end=" ") for i in range(a, b) if i % 2 == 0]

# B.py
# a = int(input())
# b = int(input()) + 1
# c = int(input())
# d = int(input())
# [print(i, end=" ") for i in range(a, b) if i % d == c]

# C.py
# from math import sqrt
# a = int(input())
# b = int(input()) + 1
# [print(i, end=" ") for i in range(a, b) if int(sqrt(i)) * int(sqrt(i)) == i]

# D.py
# x = input()
# d = input()
# cnt = int()
# for i in x:
#     if i == d:
#         cnt += 1
# print(cnt)
# print(x.count(d))

# E.py
# a = input()
# cnt = int()
# a = [int(i) for i in a]
# for i in a:
#     cnt += i
# print(cnt)

# F.py
# a = input()
# a = reversed(a)
# ok = True
# for i in a:
#     if i != '0' and ok:
#         ok = False
#         print(i, end='')
#     elif i == '0' and ok:
#         continue
#     else:
#         print(i, end='')

# G.py
# a = int(input())
# for i in range(2, a + 1):
#     if a % i == 0:
#         print(i)
#         break

# H.py
# a = int(input())
# [print(i, end=' ') for i in range(1, a + 1) if (a % i) == 0]

# I.py
# from math import sqrt
# a = int(input())
# cnt = int()
# for i in range(1, int(sqrt(a))):
#     if (a % i) == 0:
#         cnt += 2
# if int(sqrt(a)) * int(sqrt(a)) == a:
#     cnt += 1
# print(cnt)

# J.py
# cnt = int()
# for i in range(100):
#     cnt += int(input())
# print(cnt)

# K.py
# cnt = int()
# for i in range(int(input())):
#     cnt += int(input())
# print(cnt)

# L.py
# a = input()
# cnt = int()
# b = 0
# for i in a[len(a) - 1::-1]:
#     cnt += int(i) * pow(2, b)
#     b += 1
# print(cnt)

# M.py
n = int(input())
cnt = 0
for i in range(n):
    if int(input()) == 0:
        cnt += 1
print(cnt)

