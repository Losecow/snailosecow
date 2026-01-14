import sys
input = sys.stdin.readline

n = input().strip()
iron = list(n)

count = 0
ans = []

for i in range(len(iron)):
    ans.append(iron[i])

    temp = ans.pop()

    if temp == ")":
        if iron[i - 1] == "(":
            ans.pop()
            count += len(ans)
        else:
            ans.pop()
            count += 1
    else:
        ans.append(temp)

    # print("i = ", i , ",ans = ", ans, ",count = ", count)
print(count)