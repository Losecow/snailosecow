import sys
from collections import deque

input = sys.stdin.readline

N = int(input())

numList = deque([])

for i in range(N):
    x = input().split()

    if x[0] == "push":
        numList.append(x[1])
    elif x[0] == "pop":
        if len(numList) != 0:
            print(numList.popleft())
        else:
            print("-1")
    elif x[0] == "size":
        print(len(numList))
    elif x[0] == "empty":
        if len(numList) != 0:
            print("0")
        else:
            print("1")
    elif x[0] == "front":
        if len(numList) != 0:
            print(numList[0])
        else:
            print("-1")
    elif x[0] == "back":
        if len(numList) != 0:
            print(numList[-1])
        else:
            print("-1")
    
# https://docs.python.org/3/library/collections.html#collections.deque