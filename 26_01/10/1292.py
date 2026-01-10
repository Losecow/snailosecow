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


import sys
input = sys.stdin.readline

n, m = map(int, input().split())

arr = []
num = 1

while len(arr) < m:
    for _ in range(num):
        arr.append(num)
    num += 1

prefix = [0]
for x in arr:
    prefix.append(prefix[-1] + x)

print(prefix[m] - prefix[n-1])
