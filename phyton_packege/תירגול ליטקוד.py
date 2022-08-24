# I = 1
# V = 5
# X = 10                  IV = 4, IX = 9, XL = 40, XC = 90, CD = 400, CM = 900
# L = 50
# C = 100
# D = 500
# M = 1000

# str = "IV"  # 7
# count = 0
# i = 0
# dic = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
# while i < (len(str) - 1):
#     if (str[i] == 'I' and (str[i + 1] == 'V' or str[i + 1] == 'X')):
#         count += dic.get(str[i + 1]) - 1
#         i += 2

#     elif (str[i] == 'X' and (str[i + 1] == 'L' or str[i + 1] == 'C')):
#         count += dic.get(str[i + 1]) - 10
#         i += 2

#     elif (str[i] == 'C' and (str[i + 1] == 'D' or str[i + 1] == 'M')):
#         count += dic.get(str[i + 1]) - 100
#         i += 2
#     else:
#         count += dic.get(str[i])
#         i += 1
# if (i == len(str) - 1):
#     count += dic.get(str[len(str) - 1])

# print(count)

# ------------------------------------

# 2
# ransomNote = "aa"
# magazine = "aab"
#
# if ransomNote in magazine:
#     print("true")
# else:
#     print("false")

# -----------------------------------

# Fizz Buzz
# FizzBuzz - if the number divisible by 3 and 5
# Fizz - if the number divisible by 3
# Buzz - if the number divisible by 5
# i

# list1 = []
# n = int(input("enter number: "))

# for i in range(1, n+1):
#     if i%3==0 and i%5==0:
#         list1.append("FizzBuzz")
#     elif i%3==0:
#         list1.append("Fizz")
#     elif i%5==0:
#         list1.append("Buzz")
#     else:
#         list1.append(i)

# print(list1)

# ------------------------------------
# Matrix

# mat = [[1, 1, 0, 0, 0], [1, 1, 1, 1, 0], [1, 0, 0, 0, 0], [1, 1, 0, 0, 0], [1, 1, 1, 1, 1]]
# k = 3
# ans = {}
# for i in range(len(mat)):
#     ans[i] = sum(mat[i])
# ans = sorted(ans, key=ans.get)
# print(ans[:k])

# ----------------------------------

# string = "((()(((((("
# stack = []
# result = 0
# for i in range(len(string)):
#     if string[i] == ")" and len(stack) == 0:
#         pass
#     elif string[i] == "(":
#         stack.append(string[i])
#     elif string[i] == ")":
#         stack.pop(len(stack)-1)
#         result += 2

# print(result)

# ===================================

# import itertools
#
# list1 = list(itertools.permutations([1, 2, 3]))
# print(list1)

# ==========================

# strs = ["flower", "flow", "flight"]
# retList = []
#
# for i in strs:
#     if strs[]
#     elif len(strs) == 0:
#         print("")

# =========================

# nums = [2, 7, 11, 15]
# target = 9
# retList = []
# list1 = []
#
# for i in range(len(nums)):
#     for j in range(i, len(nums)):
#         if nums[i] + nums[j] == target:
#             retList.append(nums[i])
#             retList.append(nums[j])
#             list1.append(retList.index(nums[i]))
#             list1.append(retList.index(nums[j]))
# print(list1)

# ========================

# s = "(]"
#
#
# for i in range(len(s)):
#     if s[i] == "(" and s[i+1] == ")":
#         print("true")
#     elif s[i] == "[" and s[i+1] == "]":
#         print("true")
#     elif s[i] == "{" and s[i+1] == "}":
#         print("true")
#     else:
#         print("false")

# ======================

strs = ["vlower", "glow", "flight"]
stack = []
string = ""
# res = min(strs, key=len)

# for i in range(len(res)):
#     for j in range(len(strs)):
#         if res[i] != strs[j][i]:
#             if len(stack) == 0:
#                 print("")
#             else:
#                 print(string.join(stack))
#             exit()
#     stack.append(res[i])
#
#
# print(string.join(stack))

if len(strs) == 0:
    print("")
    exit()
else:
    s1 = max(strs)
    s2 = min(strs)
    i, match = 0, 0
    while i < len(s1) and i < len(s2) and s1[i] == s2[i]:
        i, match = i + 1, match + 1
    print(s1[0:match])
    exit()