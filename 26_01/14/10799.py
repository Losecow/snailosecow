import sys
input = sys.stdin.readline

n = input().strip()
iorn = list(n)

print(iorn)
count = 0

while len(iorn) != 0:

    if iorn.pop() == ")":
        count += 1
        temp = iorn.pop()
        if temp == "(":
            count -= 1
            count *= 2
        else:
            iorn.append(temp)
    else:
        count -= 1

print(count)