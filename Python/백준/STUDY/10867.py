N = int(input())
M = list(map(int, input().split()))

M = list(set(M))
M.sort()
print(M)