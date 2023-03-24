# 1
# def count_evens(nums):
#     cnt = 0
#     for i in nums:
#         if i % 2 == 0:
#             cnt += 1
#     return cnt

# 2
# def big_diff(nums):
#     return max(nums) - min(nums)

# 3
# def centered_average(nums):
#     nums.remove(max(nums))
#     nums.remove(min(nums))
#     return sum(nums) // len(nums)

# 4
# def sum13(nums):
#     if not bool(nums):
#         return 0
#     cnt = 0
#     i = 0
#     while i < len(nums):
#         if nums[i] == 13:
#             i += 2
#         else:
#             cnt += nums[i]
#             i += 1
#     return cnt

# 5
# def sum67(nums):
#     cnt = 0
#     ok = False
#     for i in nums:
#         if i == 6 and ok == False:
#             ok = True
#         elif i == 7 and ok == True:
#             ok = False
#         elif ok:
#             pass
#         else:
#             cnt += i
#     return cnt

# 6
# def has22(nums):
#     for i in range(len(nums) - 1):
#         if nums[i] == 2 and nums[i + 1] == 2:
#             return True
#     return False
