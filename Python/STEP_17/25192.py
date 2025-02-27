import sys
inpput = sys.stdin.readline

N = int(input())

userList = set()
cnt = 0

for i in range(N):
    x = input().strip()

    if x == "ENTER":
        userList.clear()
    else:
        if x not in userList:
            userList.add(x)
            cnt += 1
print(cnt)
