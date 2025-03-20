N = []

for _ in range(9):
    N.append(list(map(int, input().split())))

Max = 0
row = 0
col = 0

for i in range(9):
    for j in range(9):
        if N[i][j] > Max:
            Max = N[i][j]
            row = i
            col = j

print(Max)
print(row + 1, col + 1)