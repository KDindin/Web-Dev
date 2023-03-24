# 1
# def string_times(str, n):
#     res = ""
#     for i in range(n):
#         res += str
#     return res


# 2
# def front_times(str, n):
#     res = ""
#     for i in range(n):
#         res += str[:3]
#     return res

# 3
# def string_bits(str):
#     return str[::2]

# 4
# def string_splosion(str):
#     res = ""
#     for i in range(1, len(str) + 1):
#         res += str[:i]
#     return res

# 5
# def last2(str):
#   cnt = 0
#   for i in range(len(str) - 2):
#     if str[i] == str[-2] and str[i + 1] == str[-1]:
#       cnt += 1
#   return cnt
# 2 way)
# import re
# def last2(str):
#     print(str[-2:])
#     # return str.count(str[-2:])
#     return len(re.findall(str[-2:], str))

# 6
# def array_count9(nums):
#     return nums.count(9)

# 7
# def array_front9(nums):
#     for i in range(min(4, len(nums))):
#         if nums[i] == 9:
#             return True
#     return False

# 8
# def array123(nums):
#     for i in range(len(nums) - 1):
#         if nums[i - 1] == 1 and nums[i] == 2 and nums[i + 1] == 3:
#             return True
#         else:
#             i += 3
#     return False

# 9
# def string_match(a, b):
#     ok = False
#     seq = 0
#     cnt = 0
#     for i in range(min(len(a), len(b))):
#         if a[i] == b[i] and ok == False:
#             seq += 1
#             ok = True
#         elif a[i] == b[i] and ok == True:
#             seq += 1
#             if seq >= 2:
#                 cnt += 1
#         elif a[i] != b and ok == True:
#             ok = False
#         else:
#             pass
#     return cnt
