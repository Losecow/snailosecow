N = []
M = int(input())

for i in range(M):
    N.append(int(input()))

N.sort()

for i in range(len(N)):
    print(N[i])