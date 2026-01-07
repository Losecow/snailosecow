import sys
input = sys.stdin.readline

n = int(input())

count = 0

dp = [0] * (n + 1)
    
dp[1] = 0

for i in range(2, n + 1):

    if i % 3 == 0 and i % 2 == 0:
        temp_3 = i // 3
        temp_2 = i // 2
        dp[i] = min(dp[i - 1], dp[temp_3], dp[temp_2]) + 1

    elif i % 3 == 0:
        temp_3 = i // 3
        dp[i] = min(dp[i - 1], dp[temp_3]) + 1

    elif i % 2 == 0:
        temp_2 = i // 2
        dp[i] = min(dp[i - 1], dp[temp_2]) + 1

    else:
        dp[i] = dp[i - 1] + 1

# print(dp)
print(dp[n])


# import sys
# input = sys.stdin.readline

# n = int(input())

# count = 0

# while(1):
#     if n == 1:
#         break
#     count += 1

#     if n % 3 == 0 and n % 2 == 0:
#         n = min(n - 1, n // 3, n // 2)
#     elif n % 3 == 0 and n % 2 != 0:
#         n = min(n - 1, n // 3)
#     elif n % 3 != 0 and n % 2 == 0:
#         n = min(n - 1, n // 2)
#     else:
#         n -= 1

#     # print("count = ", count, "n = ", n)

# print(count)