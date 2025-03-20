point = {}

for i in range(1, 9):
    x = int(input())
    point[x] = i

pointSort = sorted(point.items(), reverse = True)

sumPoint = sum(P[0] for P in pointSort[:5])
listPoint = [P[1] for P in pointSort[:5]]
listPoint.sort()

print(sumPoint)
print(*listPoint)