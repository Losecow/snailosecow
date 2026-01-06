# import sys
# input = sys.stdin.readline

# n = int(input())

# arr = [int(input()) for _ in range(n)]
# rev_arr = arr[::-1]

# rev_arr.append(int(0))

# # print(rev_arr)

# point = 0
# count = 0

# for i in range(n):
#     if rev_arr[i] == 0:
#         # print(point)
#         break
#     if rev_arr[i] > rev_arr[i + 1] or count == 1 :
#         # print(rev_arr[i], rev_arr[i + 1])
#         point += rev_arr[i]
#         # print("point = ", point)
#         count = 0
#     else:
#         count += 1
#         # print(count)
#         continue

# print(point)


import sys
input = sys.stdin.readline

n = int(input())
stairs = [0] + [int(input()) for _ in range(n)]

# 예외 처리
if n == 1:
    print(stairs[1])
    exit()
if n == 2:
    print(stairs[1] + stairs[2])
    exit()

dp = [0] * (n + 1)

dp[1] = stairs[1]
dp[2] = stairs[1] + stairs[2]

for i in range(3, n + 1):
    dp[i] = max(
        dp[i - 2] + stairs[i],          
        dp[i - 3] + stairs[i - 1] + stairs[i]  
    )

print(dp[n])
