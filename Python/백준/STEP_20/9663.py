import sys
input = sys.stdin.readline

n = int(input())

count = 0
arr = [[0 for _ in range(n)] for _ in range(n)]

def queen(n):
    for i in range(n):
        arr[i * (n + 1)] = 1
        arr[i * (n - 1)] = 1


queen(n)