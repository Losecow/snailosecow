import sys
input = sys.stdin.readline

n = int(input())

bestseller = {}

for _ in range(n):
    name = input().strip()

    if name not in bestseller:
        bestseller[name] = 1
    else:
        bestseller[name] += 1

    # bestseller[name] = bestseller.get(name, 0) + 1

items = bestseller.items() # 딕셔너리의 값들을 튜플형태로 전환

sorted_items = sorted(items, key=lambda x: (-x[1], x[0]))

print(sorted_items[0][0])

