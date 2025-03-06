import sys
input = sys.stdin.readline

N = int(input())

grade = []

for i in range(N):
    x = input().rstrip()
    grade.append(x)

grade.sort()

for i in range(7):
    print(grade[i])