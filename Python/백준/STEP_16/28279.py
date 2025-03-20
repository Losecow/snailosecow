import sys
from collections import deque
input = sys.stdin.readline

N = int(input())
numList = deque([])

for i in range(N):
    x = input().split()

    if x[0] == "1":
        numList.appendleft(x[1])
    elif x[0] == "2":
        numList.append(x[1])
    elif x[0] == "3":
        if numList:
            print(numList.popleft())
        else:
            print("-1")
    elif x[0] == "4":
        if numList:
            print(numList.pop())
        else:
            print("-1")
    elif x[0] == "5":
        print(len(numList))
    elif x[0] == "6":
        if numList:
            print("0")
        else:
            print("1")
    elif x[0] == "7":
        if numList:
            print(numList[0])
        else:
            print("-1")
    elif x[0] == "8":
        if numList:
            print(numList[-1])
        else:
            print("-1")