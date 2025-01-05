N = int(input())
M = int(input())

primeNum = []

for i in range(N, M + 1):
    primeNum.append(i)
    if i == 1:
        primeNum.remove(i)

for i in range(N, M + 1):
    for j in range(2, i):
        if i % j == 0:
            primeNum.remove(i)
            break

if len(primeNum) >= 1:
    print(sum(primeNum))
    print(min(primeNum))
else:
    print("-1")