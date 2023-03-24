# 1.
# print("Hello, World!")

# 2
# import math
# import os
# import random
# import re
# import sys
#
#
#
# if __name__ == '__main__':
#     n = int(input().strip())
#     if (n % 2 == 1) or (n % 2 == 0 and 6 <=n and n<= 20):
#         print('Weird')
#     elif (2 <= n and n <= 5 and n % 2 == 0) or (n%2==0 and n>20):
#         print('Not Weird')

# 3
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a + b)
#     print(a - b)
#     print(a * b)

# 4
# if __name__ == '__main__':
#     a = int(input())
#     b = int(input())
#     print(a // b)
#     print(a / b)

# 5
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(n):
#         print(pow( i, 2))

# 6
# def is_leap(year):
#     leap = False
#
#     # Write your logic here
#     if (year % 4 == 0 and year % 100 != 0) or year % 400 == 0:
#         leap = True
#     return leap
#
#
# year = int(input())
# print(is_leap(year))

# 7
# if __name__ == '__main__':
#     n = int(input())
#     for i in range(1, n + 1):
#         print(i, end = "")

# 8
# n = int(input())
# s = input().split()
# a = dict()
# # for index, i in s:
# #     if index == len(s):
# #         break
# #     a[int(i)] += 1
# # for i in a.keys:
# #     if a[i] != n:
# #         print(i)
# for i in s:
#     a[int(i)] += 1
# print(a)                      // is not completed

# 9
# def print_formatted(number):
#     l = len(bin(number).replace("0b", ""))
#     for i in range(1, number + 1):
#         print("{0:>{1}} {2:>{1}} {3:>{1}} {4:>{1}}".format(
#             i,
#             l,
#             oct(i).replace("0o", ""),
#             hex(i).replace("0x", "").upper(),
#             bin(i).replace("0b", "")
#         ))
#
#
# if __name__ == '__main__':
#     n = int(input())
#     print_formatted(n)

# 10
# if __name__ == '__main__':
#     x = int(input())
#     y = int(input())
#     z = int(input())
#     n = int(input())
#     newlist = [[i, j, k]
#                for i in range(x + 1)
#                for j in range(y + 1)
#                for k in range(z + 1)
#                if i + j + k != n]
#     print(newlist)

# 11
if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    arr = list(arr)
    maxi = max(arr)
    arr = [k for k in arr if k != maxi]
    print(max(arr))
