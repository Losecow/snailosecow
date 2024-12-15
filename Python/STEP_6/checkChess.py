chess = [1, 1, 2, 2, 2, 8]
lost = list(map(int, input().split()))

for i in range(len(chess)):
    if chess[i] != lost[i]:
        lost[i] = chess[i] - lost[i]
    else:
        lost[i] = 0
        
print(*lost)
