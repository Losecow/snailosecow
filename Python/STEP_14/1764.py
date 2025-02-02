import sys
input = sys.stdin.readline

N, M = map(int, input().split())

name_dict = {}
cnt = 0

for i in range(N):
    x = input().rstrip()
    name_dict[x] = 1

for i in range(M):
    x = input().rstrip()
    if x in name_dict:
        name_dict[x] += 1
    else:
        name_dict[x] = 1

for key, value in name_dict.items():
    if value > 1:
        cnt += 1

name_print = [key for key, value in name_dict.items() if value > 1]
name_print.sort()

print(cnt)
for item in name_print:
    print(item)