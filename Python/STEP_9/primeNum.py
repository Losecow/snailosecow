N = int(input())

num = list(map(int, input().split()))

for i in range(N):
    if num[i] == 1:
        N -= 1
    else:
        for j in range(2, num[i]):
            if num[i] % j == 0:
                N -= 1
                break
            else:
                continue
print(N)