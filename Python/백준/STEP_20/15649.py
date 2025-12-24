# import sys
# input = sys.stdin.readline

# def backtracking():
#     if len(array) == m:
#         print(" ".join(map(str, array)))
#         return

#     for i in range(1, n+1):
#         if i not in array:
#             array.append(i)
#             backtracking()
#             array.pop()

# n, m = map(int,input().split())
# array = []

# backtracking()

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
        start = i
        backtracking(start)
        array.pop()

backtracking(n)