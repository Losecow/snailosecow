N, K = map(int, input().split())

num = [i + 1 for i in range(N)]

#print(num)

for i in range(K):
    A, B = map(int, input().split())
    temp = num[A - 1]
    num[A - 1] = num[B - 1]
    num[B - 1] = temp
#    print(num)

print(*num)
