N, K = map(int, input().split())

num = list(map(int, input().split()))
num.sort()

print(num[K - 1])

# point is, when you want to get numbers in one line, you should use 'list'
