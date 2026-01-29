import sys

input = sys.stdin.readline

n, m = map(int, input().split())

min_edges = n - 1
max_edges = 2 * n - 3

if m < min_edges or m > max_edges:
    print(-1)
    sys.exit(0)

edges = []

# Build a star centered at 1: sums 3..n+1 (all distinct)
for i in range(2, n + 1):
    edges.append((1, i))

extra = m - (n - 1)
if extra > 0:
    # Use edges (k, n) for k=2..n-1: sums n+2..2n-1 (distinct)
    for k in range(2, n):
        if extra == 0:
            break
        edges.append((k, n))
        extra -= 1

out = "\n".join(f"{a} {b}" for a, b in edges)
print(out)
