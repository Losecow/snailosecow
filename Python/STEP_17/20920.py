import sys
input = sys.stdin.readline

N, M = map(int, input().rstrip().split())
ENG = {}

for i in range(N):
    x = input().rstrip()

    if len(x) < M:
        continue
    else:
        if x in ENG:
            ENG[x] += 1
        else:
            ENG[x] = 1

ENG = sorted(ENG.items(), key = lambda x:(-x[1], -len(x[0]), x[0]))

for i in ENG:
    print(i[0])
