import sys
import math
input = sys.stdin.readline

N = int(input())

tree = []
distence = []

for i in range(N):
    tree.append(int(input()))
# print(tree)

for i in range(N - 1):
    distence.append(tree[i + 1] - tree[i])
# print(distence)

gcd_distence = distence[0]

for i in range(len(distence)):
    gcd_distence = math.gcd(distence[i], gcd_distence)
    # print(gcd_distence)

# print(tree[len(tree) - 1], tree[0], gcd_distence)

result = (tree[N - 1] - tree[0]) // gcd_distence - 1 - N + 2
print(result)