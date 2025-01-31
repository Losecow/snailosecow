import sys
input = sys.stdin.readline

N = int(input())

commute = {}

for i in range(N):
    x, y = map(str, input().split())
    if y == "enter":
        commute[x] = y
    elif y == "leave":
        if x in commute:
            del commute[x]
        else:
            continue

commute = sorted(commute.keys(), reverse = True)

for key in commute:
    print(key)
