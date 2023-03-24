# 4.
# A.py
# a = int(input())
# b = 1
# while b * b <= a:
#     print(b * b)
#     b += 1

# B.py
# a = int(input())
# b = 2
# while a % b != 0:
#     b += 1
# print(b)

# C.py
# a = int(input())
# b = 2
# print(1, end=' ')
# while a >= b:
#     print(b, end=' ')
#     b *= 2

# D.py
# a = int(input())
# if a % 2 == 1 and a != 1:
#     print('NO')
#     exit()
# while a % 2 != 1:
#     a /= 2
# if a % 2 == 1 and a != 1:
#     print('NO')
# else:
#     print('YES')

# E.py
a = int(input())
b = 1
cnt = 0
while a > b:
    cnt += 1
    b *= 2
print(cnt)





