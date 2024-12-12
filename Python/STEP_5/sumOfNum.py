N = int(input())
M = int(input())

temp = 0

for _ in range(N):
    temp += M % 10
    M = M // 10

print(temp)
