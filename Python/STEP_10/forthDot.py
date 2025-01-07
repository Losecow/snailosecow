recDotX = []
recDotY = []
ans = []

for _ in range(3):
    X, Y = input().split()
    recDotX.append(X)
    recDotY.append(Y)

if recDotX.count(min(recDotX)) > 1:
    ans.append(max(recDotX))
else:
    ans.append(min(recDotX))

if recDotY.count(min(recDotY)) > 1:
    ans.append(max(recDotY))
else:
    ans.append(min(recDotY))    

print(*ans)