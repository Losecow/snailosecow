N = int(input())

arr = []

arr = list(map(int, input().split()))

#print(arr)

M = max(arr)
sumA = 0
for i in range(N):
    arr[i] = arr[i] / M * 100
#    print(arr[i])
    sumA += arr[i]

V = sumA / N

print(V)

