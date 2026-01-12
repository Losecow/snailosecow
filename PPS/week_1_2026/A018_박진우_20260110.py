n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
a.sort()
s = 0
for i in range(n):
    bmax = max(b)
    s += a[i] * bmax
    b.remove(bmax)

print(s)