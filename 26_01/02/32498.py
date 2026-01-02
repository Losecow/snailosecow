n = int(input())

count = 0

for _ in range(n):
    m = int(input())
    if m % 2 == 1:
        count += 1

print(count)