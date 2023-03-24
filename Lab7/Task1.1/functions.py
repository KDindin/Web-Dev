# 6.
# A.py
# def mini(fs, sd, td, fh):
#     return min(fs, sd, td, fh)
#
#
# f, s, t, fr = input().split(' ')
# print(mini(int(f), int(s), int(t), int(fr)))

# B.py
# def degree(b, n):
#     # print(b, n)
#     if n == 1:
#         return b
#     else:
#         b *= b
#         return degree(b, n - 1)
#
#
# a = input().split()
# if int(a[1]) == 0:
#     print(1)
#     exit()
# print(degree(int(a[0]), int(a[1])))
# 6.
# A.py
# def mini(fs, sd, td, fh):
#     return min(fs, sd, td, fh)
#
#
# f, s, t, fr = input().split(' ')
# print(mini(int(f), int(s), int(t), int(fr)))

# B.py
# def degree(b, n):
#     return pow(b, n)
#
#
# a = input().split()
# print(degree(float(a[0]), int(a[1])))

# C.py
def xor(c, b):
    return int(c) ^ int(b)


a = input().split()
# print(xor(int(a[0], int(a[1]))))
print(xor(a[0], a[1]))
