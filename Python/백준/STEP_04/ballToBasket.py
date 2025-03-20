N, K = map(int, input().split())

num = [0 for i in range(N)]

#print(num)

for i in range(K):
    A, B, C = map(int, input().split())
    for j in range(A - 1, B):
        num[j] = C
#       print(num)

print(*num)
