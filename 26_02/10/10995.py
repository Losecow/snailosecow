n = int(input())

for i in range(1, n + 1):
    if i % 2 == 1:

        for j in range(1, 2 * n + 1):
            if j % 2 == 1:
                print("*", end="") 
            else:
                print(" ", end="")
        print()
    else:

        print(" ", end="")
        for j in range(1, 2 * n + 1):
            if j % 2 == 1:
                print("*", end="") 
            else:
                print(" ", end="") 
        print()
