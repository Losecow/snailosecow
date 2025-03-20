N, K = map(int, input().split())

num = list(map(int, input().split()))

num.sort(reverse=True)

print(num[K - 1])