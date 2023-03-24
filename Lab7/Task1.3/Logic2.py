# 1
# def make_bricks(small, big, goal):  # big   big, small  small
#     if goal % 5 == 0 and goal / 5 <= big:
#         return True
#     elif goal / 5 >= big:
#         if goal - big * 5 > small:
#             return False
#         return True
#     elif goal / 5 < big:
#         if goal % 5 > small:
#             return False
#     return True
import math


# 2
# def lone_sum(a, b, c):
#     if b == c == a:
#         return 0
#     elif a == b:
#         return c
#     elif a == c:
#         return b
#     elif b == c:
#         return a
#     else:
#         return a + b + c

# 3
# def lucky_sum(a, b, c):
#     if a == 13:
#         return 0
#     elif b == 13:
#         return a
#     elif c == 13:
#         return a + b
#     return a + b + c

# 4
# def no_teen_sum(a, b, c):
#     return fix_teen(a) + fix_teen(b) + fix_teen(c)
#
#
# def fix_teen(n):
#     if n == 15 or n == 16:
#         return n
#     elif n in range(13, 20):
#         return 0
#     return n

# 5
# def round_sum(a, b, c):
#     return int(round10(a) + round10(b) + round10(c))
#
#
# def round10(num):
#     if num % 10 >= 5:
#         if 5 <= num < 10:
#             return 10
#         return (round(num / 10 + 1)) * 10
#     return round(num / 10) * 10

# 6
# def close_far(a, b, c):
#     if abs(a - b) <= 1 and abs(b - c) >= 2 and abs(a - c) >= 2:
#         return True
#     if abs(a - c) <= 1 and abs(b - c) >= 2 and abs(a - b) >= 2:
#         return True
#     return False

# 7
# def make_chocolate(small, big, goal):
#     if goal % 5 == 0 and goal / 5 <= big:
#         return 0
#     elif goal / 5 >= big:
#         if goal - big * 5 > small:
#             return -1
#         return goal - big * 5
#     elif goal / 5 < big:
#         if goal % 5 > small:
#             return -1
#     return goal % 5

