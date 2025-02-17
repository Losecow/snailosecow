K = int(input())

moneyCount = []

for i in range(K):
    x = int(input())
    if x == 0:
        moneyCount.pop()
    else:
        moneyCount.append(x)

print(sum(moneyCount))