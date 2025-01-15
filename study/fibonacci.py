F = []
F.append(int(0))
F.append(int(1))

N = int(input())

for i in range(2, N + 1):
    F.append(int(F[i - 2] + F[i - 1]))

print(F[N])