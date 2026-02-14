a, b, c = map(int, input().split())

case1 = (a * b) / c
case2 = (a / b) * c

print(int(max(case1, case2)))