import sys
from collections import deque

input = sys.stdin.readline

N = int(input())  
balloon = deque(enumerate(map(int, input().split()), start=1))  
result = []

while balloon:
    index, move = balloon.popleft() 
    result.append(index) 

    if balloon:  
        if move > 0:
            balloon.rotate(-(move - 1)) 
        else:
            balloon.rotate(-move) 

print(*result)  