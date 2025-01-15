# def sieve_of_eratosthenes(N):
#     primeNum = [True] * (N + 1)
#     primeNum[0] = primeNum[1] = False  

#     for i in range(2, int(N**0.5) + 1):
#         if primeNum[i]:  
#             for j in range(i * i, N + 1, i):  
#                 primeNum[j] = False  

#     primeNum = [i for i in range(2, N + 1) if primeNum[i]]
#     return primeNum

# N = int(input())

# primeNum = sieve_of_eratosthenes(N)
# cnt = 0

# while True:
#     if N % primeNum[cnt] == 0:
#         print(primeNum[cnt])
#         N = N // primeNum[cnt]
#     else:
#         cnt += 1
#     if N == 1:
#         break

# 런타임에러 (제한시간 1초 초과)

N = int(input())

if N == 1:
    print('')

for i in range(2, N + 1):
    if N % i == 0:
        while N % i == 0:
            print(i)
            N = N / i