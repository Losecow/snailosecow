N = int(input())

num = []

while True:
    num.append(N % 10)
    N = N // 10
    if N == 0:
        break

num.sort(reverse = True)

print(*num, sep = "")