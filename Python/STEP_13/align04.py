import sys
N = int(input())

num = []

for i in range(N):
    num.append(int(sys.stdin.readline()))

num.sort()

for i in range(N):
    print(num[i])