# answer code

N = int(input())
for i in range(1,N):
    print(' '*(N-i) + '*'*(2*i-1))
for j in range(N,0,-1):
    print(' ' *(N-j)+'*'*(2*j-1))

# my code

N = int(input())

cnt = 1

for i in range(N):
    for j in range(N - cnt):
        print(" ", end = "")
    for j in range(cnt):
        print("*", end = "")
    for j in range(cnt - 1):
        print("*", end = "")
    print()
    cnt += 1

cnt = 1

for i in range(N -1):
    for j in range(cnt):
        print(" ", end = "")
    for j in range(N - cnt):
        print("*", end = "")
    for j in range(N - 1 - cnt):
        print("*", end = "")
    print()
    cnt += 1
    
