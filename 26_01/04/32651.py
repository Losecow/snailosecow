import sys
input = sys.stdin.readline

n = int(input())

start = 2024
end = 100000

arr = [i for i in range(start, end + 1, start)]

if n in arr:
    print("Yes")
else:
    print("No")