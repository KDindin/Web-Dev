# 1
# def double_char(str):
#     res = ""
#     for i in str:
#         res += i + i
#     return res

# 2
# def count_hi(str):
#     return str.count('hi')

# 3
# def cat_dog(str):
#     if str.count('dog') == str.count('cat'):
#         return True
#     return False

# 4
# def count_code(str):
#     cnt = 0
#     for i in range(2, len(str) - 1):
#         if str[i - 2] == 'c' and str[i - 1] == 'o' and str[i + 1] == 'e':
#             cnt += 1
#     return cnt

# 5
# def end_other(a, b):
#     a = a.lower()
#     b = b.lower()
#     if a[-len(b):] == b or b[-len(a):] == a:
#         return True
#     return False

# 6
# def xyz_there(str):
#     if str.count('xyz') - str.count('.xyz') > 0:
#         return True
#     return False
