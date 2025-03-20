import sys
input = sys.stdin.readline

N = int(input())
userList = {'ChongChong'}

for i in range(N):
    a, b = input().rstrip().split()

    if a in userList:
        userList.add(b)

    if b in userList:
        userList.add(a)

print(len(userList))
