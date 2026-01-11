import sys
input = sys.stdin.readline

n = int(input())

arr = list(map(int, input().split()))
ans = []
top = []
count = 0

ans.append(arr[0])

for i in range(1, n):
    ans.append(arr[i])

    if arr[i - 1] < arr[i]:
        ans.pop(i - 1)
        top.append(count)
    else:
        top.append(count)
        count += 1

print(top)