N, K = map(int, input().split())

temp = 0
factor = []

while True:
    temp += 1
    if N % temp == 0:
        factor.append(temp)
    if N == temp:
        break

if len(factor) >= K:
    print(factor[K - 1])
else:
    print("0")
