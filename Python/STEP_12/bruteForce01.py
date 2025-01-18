N, M = map(int, input().split())

cardNum = []

cardNum = list(map(int, input().split()))

a = 0
b = 0
c = 0
maxSum = -1

# aB = 0
# bB = 0
# cB = 0

for i in range(N):
    a = cardNum[i]
    for j in range(i + 1, N):
        b = cardNum[j]
        for k in range(j + 1, N):
            c = cardNum[k]
            if a + b + c > maxSum and a + b + c <= M: 
                maxSum = a + b + c
                # aB = i
                # bB = j
                # cB = k

print(maxSum)
# print(aB, bB, cB)
            
