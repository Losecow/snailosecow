# import sys
# input = sys.stdin.readline

# n, m = map(int, input().split())

# count = 0
# ans = 0
# arr = []

# for i in range(1, m + 1):
#     count += 1
#     for j in range(i):
#         ans += count
#         arr.append(ans)
    
# print(arr[m - 1] - arr[n - 2]) 여기가 틀림 (n == 1 일때 고려 안함)
# # print(arr)