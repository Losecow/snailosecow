N, M = map(int, input().split())

primeNum = list(True for _ in range(M + 1))
primeNum[0] = False
primeNum[1] = False

for i in range(2, int(M ** (1 / 2)) + 1):
    if primeNum[i]:
        for j in range(i * 2, M + 1, i): 
            primeNum[j] = False

for i in range(N, M + 1):
    if primeNum[i] == True:
        print(i)