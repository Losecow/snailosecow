import sys
input = sys.stdin.readline

n, m = map(int,input().split())
array = []


def backtracking(start):
    
    if len(array) == m:
        print(" ".join(map(str, array)))
        return

    for i in range(start, n + 1):
        array.append(i)
        backtracking(1)
        array.pop()

backtracking(1)