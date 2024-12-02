aggregate = int(input())

N = int(input())
sum = 0

for i in range(N):
    price, quantity = map(int, input().split())
    sum += price * quantity

if aggregate == sum:
    print("Yes")
else:
    print("No")
