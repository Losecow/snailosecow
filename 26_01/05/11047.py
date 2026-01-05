# import sys

# input = sys.stdin.readline

# n, m = map(int, input().split())

# arr = []
# num = 0

# for i in range(n):
#     num = int(input())
#     arr.append(num)

# # print(arr)

# count = 0
# count_m = 0

# # for i in range(n - 1, -1, -1):
# #     print("i :", arr[i])

# for i in range(n - 1, -1, -1):
#     if m >= arr[i]:
#         while count_m < m:
#             count_m += arr[i]
#             count += 1
#     if count_m > m:
#         if count_m == m:
#             break
#         else:
#             count_m -= arr[i]
#             count -= 1 

#     # print(arr[i], i)

# # print(count_m, count)
# print(count)


import sys
input = sys.stdin.readline

n, m = map(int, input().split())
arr = [int(input()) for _ in range(n)]

count = 0

for i in range(n - 1, -1, -1):
    if m == 0:
        break
    use = m // arr[i] 
    count += use
    m -= use * arr[i]

print(count)
