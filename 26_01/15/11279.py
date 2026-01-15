# import sys
# input = sys.stdin.readline

# n = int(input())

# arr = []

# for i in range(n):
#     m = int(input())
#     arr.sort()

#     if len(arr) == 0:
#         if m != 0:
#             arr.append(m)
#         else:
#             print("0")

#     else:
#         if m == 0:
#             print(arr.pop())

#         else:
#             temp = arr.pop()

#             if temp < m:
#                 arr.append(temp)
#                 arr.append(m)
#             else:
#                 arr.append(m)
#                 arr.append(temp)


import sys
input = sys.stdin.readline

n = int(input())
arr = []

for _ in range(n):
    m = int(input())

    if m == 0:
        if arr:
            print(arr.pop())   
        else:
            print("0")
    else:
        i = len(arr) - 1
        while i >= 0 and arr[i] > m:
            i -= 1
        arr.insert(i + 1, m)


