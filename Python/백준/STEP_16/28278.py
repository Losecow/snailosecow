import sys
input = sys.stdin.readline

N = int(input())

numList = []

for i in range(N):
    x = input().split()

    if x[0] == "1":
        numList.append(x[1])
    elif x[0] == "2":
        if numList:
            print(numList.pop())
        else:
            print(-1)
    elif x[0] == "3":
        print(len(numList))
    elif x[0] == "4":
        if numList:
            print(0)
        else:
            print(1)
    elif x[0] == "5":
        if numList:
            print(numList[-1])
        else:
            print(-1)