N = int(input())

cX = []
cY = []

for i in range(N):
    X, Y = map(int, input().split())

    cX.append(X)
    cY.append(Y)

print((max(cX) - min(cX)) * (max(cY) - min(cY)))