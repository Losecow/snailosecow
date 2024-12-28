N = int(input())

cnt = 2

for _ in range(N):
    cnt += cnt - 1

print(cnt * cnt)  