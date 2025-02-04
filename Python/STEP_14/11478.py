N = input()
total = set()
for i in range(len(N)):
    for j in range(i, len(N)):
        total.add(N[i : j + 1])

print(len(total))

#내일다시