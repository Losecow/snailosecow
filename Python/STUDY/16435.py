N, L = map(int, input().split())
h = list(map(int, input().split()))

h.sort()

for i in range(N):
    if h[i] <= L:
        L += 1
        continue
    else:
        break

print(L)
