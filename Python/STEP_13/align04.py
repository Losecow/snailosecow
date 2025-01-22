# import sys
# N = int(input())

# num = []

# for i in range(N):
#     num.append(int(sys.stdin.readline()))

# num.sort()

# for i in range(N):
#     print(num[i])

# 메모리초과
    

import sys
input = sys.stdin.readline

n = int(input())
arr = [0] * (10000 + 1) 

for _ in range(n):
    arr[int(input())] += 1
  
for i in range(len(arr)):
    if arr[i] != 0: 
        for _ in range(arr[i]):
            print(i)