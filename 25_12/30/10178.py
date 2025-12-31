n = int(input())

for _ in range(n):
    candy, baby = map(int, input().split())
    print("You get " + str(candy // baby) + " piece(s) and your dad gets " + str(candy % baby) + " piece(s).")