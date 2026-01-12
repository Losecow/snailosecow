nums = list(map(int, input().split()))
total = sum(x**2 for x in nums)
print(total % 10)