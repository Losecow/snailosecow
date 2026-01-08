# import sys
# input = sys.stdin.readline

# n, k = map(int, input().split())

# y = [i for i in range(1, n + 1)]

# ans = []

# check = 0

# while(1):

#     if len(y) == 1:
#         ans.append(y.pop())
#         break

#     for i in range(len(y)):
#         if len(y) <= i:
#             check += 1
#             break
#         if check == k:
#             ans.append(y.pop(i))
#             check = 0
#         check += 1
    
# print(ans)



import sys
input = sys.stdin.readline

n, k = map(int, input().split())

y = [i for i in range(1, n + 1)]

ans = []

idx = 0

while(1):
    if len(y) == 1:
        ans.append(y.pop())
        break

    idx = (idx + k - 1) % len(y)
    ans.append(y.pop(idx))

print("<" + ", ".join(map(str, ans)) + ">")


