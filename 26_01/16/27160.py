n = int(input())

card = {}
boolean = 0

for _ in range(n):
    fruit, count = input().split()

    card[fruit] = card.get(fruit, 0) + int(count)

for fruit in card:
    if card[fruit] == 5:
        boolean = 1

if boolean == 1:
    print("YES")
else:
    print("NO")


# card.values() 를 쓰자!!!!!

# if 5 in card.values():
#     print("YES")
# else:
#     print("NO")

