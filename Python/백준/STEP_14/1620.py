import sys
input = sys.stdin.readline

N, M = map(int, input().split())

poketmonName = {}
poketmonNum = {}

# 개천재발상  -> 딕셔너리에 이름:번호, 번호:이름 두가지를 저장하면 되잖아???

for i in range(1, N + 1):
    x = input().rstrip()
    poketmonNum[i] = x
    poketmonName[x] = i

for i in range(M):
    x = input().rstrip()
    if x.isdigit():
        print(poketmonNum[int(x)])
    else:
        print(poketmonName[x])