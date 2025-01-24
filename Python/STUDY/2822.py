point = {}

for i in range(1, 9):
    x = int(input())
    point[x] = i

print(point)

pointSort = sorted(point.items(), reverse = True)
# point1 = sorted(point, reverse = True)

print(point1)

sumPoint = 0
temp = 0
cnt = 0

for i in range(5):
    sumPoint += pointSort