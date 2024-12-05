N = int(input())

for i in range(N):
    for j in range(i + 1):
        print("*", sep = "", end = "")
    print("\n", end ="")
