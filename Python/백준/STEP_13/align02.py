num = []
for i in range(5):
    num.append(int(input()))

print(sum(num) // 5)

num.sort()

print(num[len(num) // 2])
