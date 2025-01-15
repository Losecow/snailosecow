N = int(input())

count = 1

for i in range(N):
    for j in range(N - count):
        print(" ", sep = "", end = "")
    for j in range(count):
        print("*", sep = "", end = "")
    count += 1
    print("\n", end = "")
