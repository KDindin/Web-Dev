# 5.
# A.py
# input()
# b = input()
# for i, b in enumerate(b.split(' ')):
#     if i % 2 == 0:
#         print(b, end=' ')

# B.py
# input()
# b = input()
# for i in b.split(' '):
#     if int(i) % 2 == 0:
#         print(i, end=' ')

# C.py
# input()
# cnt = 0
# b = input()
# for i in b.split(' '):
#     if int(i) > 0:
#         cnt += 1
# print(cnt)

# D.py
# input()
# b = input().split()
# prev = int()
# cnt = 0
# for index, i in enumerate(b):
#     if index == 0:
#         prev = int(i)
#         continue
#     if int(i) > prev:
#         cnt += 1
#     prev = int(i)
# print(cnt)

# E.py
# input()
# b = input().split()
# prev = int()
# for index, i in enumerate(b):
#     if index == 0:
#         prev = int(i)
#         continue
#     if (prev < 0 and int(i) < 0) or (prev > 0 and int(i) > 0):
#         print('YES')
#         exit()
#     prev = int(i)
# print('NO')

# F.py
# n = int(input())
# b = input().split()
# cnt = int()
# for i in range(1, n - 1):
#     if int(b[i - 1]) < int(b[i]) and int(b[i]) > int(b[i + 1]):
#         cnt += 1
# print(cnt)

# G.py
input()
b = input().split(' ')
b.reverse()
for i in b:
    print(int(i), end=" ")
