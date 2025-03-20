import sys
input = sys.stdin.readline

N = int(input())

coordinate_list = []

for i in range(N):
    coordinate_list.append(list(map(int, input().split())))

coordinate_list.sort(key = lambda x : (x[1], x[0]))

for i in range(N):
    print(*coordinate_list[i])