import sys
input = sys.stdin.readline

parenthesis_string = [] #PS

N = int(input())

for i in range(N):
    x = list(map(str, input().split()))
    for j in range(len(x)):
        if x[j] == "(" and x[j + 1] == ")":
            x.pop(j)
            x.pop(j + 1)
    parenthesis_string.append(x)

print(parenthesis_string)