N = int(input())
M = [[0 for col in range(100)] for row in range(100)]

for i in range(N):
    x, y = map(int, input().split())

    for y_M in range(y, y + 10):
        for x_M in range(x, x + 10):
            M[y_M][x_M] = 1

cnt = 0 
for k in range(100): 
    cnt += M[k].count(1)

print(cnt)