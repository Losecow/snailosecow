N = int(input())

for i in range(1, N + 1):
    if sum(map(int, str(i))) + int(i) == N:
        print(i)
        break
    elif i == N:
        print(0)
    
