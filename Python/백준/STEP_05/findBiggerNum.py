N, M = input().split()

N = N[::-1]
M = M[::-1]

N = int(N)
M = int(M)

if N > M:
    print(N)
else:
    print(M)
