from collections import deque
import sys
input = sys.stdin.readline

n = int(input())

d = deque()

temp = 0

for _ in range(n):
    data = input().split()

    if len(data) == 2:
        line = data[0]
        x = int(data[1])

        if line == "push_front":
            d.appendleft(x)
    
        elif line == "push_back":
            d.append(x)
    
    else:
        line = data[0]

        if line == "pop_front":
            if len(d) == 0:
                print("-1")
            else:
                print(d.popleft())

        elif line == "pop_back":
            if len(d) == 0:
                print("-1")
            else:
                print(d.pop())

        elif line == "size":
            print(len(d))

        elif line == "empty":
            if len(d) == 0:
                print("1")
            else:
                print("0")

        elif line == "front":
            if len(d) == 0:
                print("-1")
            else:
                temp = d.popleft()
                print(temp)
                d.appendleft(temp)

        elif line == "back":
            if len(d) == 0:
                print("-1")
            else:   
                temp = d.pop()
                print(temp)
                d.append(temp)