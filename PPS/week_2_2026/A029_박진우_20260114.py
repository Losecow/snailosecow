n = int(input())
first = int(input())

if n > 5:
    print("LOVE")
else:
    if (first == 1 and n % 2 == 1) or (first == 0 and n % 2 == 0):
        print("LOVE")
    else:
        print("OH MY GOD")
