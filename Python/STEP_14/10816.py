import sys
input = sys.stdin.readline

N = int(input())
firstLine = list(map(int,input().split()))
M = int(input())
secondLine = list(map(int,input().split()))

num_Dict = {}

for i in firstLine:
    if i in num_Dict:
        num_Dict[i] += 1
    else:
        num_Dict[i] = 1

for i in secondLine:
    if i in num_Dict:
        print(num_Dict[i], end = ' ')
    else:
        print(0, end = ' ')