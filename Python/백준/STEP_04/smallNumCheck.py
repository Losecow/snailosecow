N, X = map(int, input().split())

A = list(map(int, input().split()))
B = []

for i in range(N):
    if A[i] < X:
        B.append(A[i])
        
print(*B)
