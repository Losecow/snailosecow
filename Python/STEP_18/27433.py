def factorial(N):
    if N > 1:
        return N * factorial(N - 1)
    else:
        return 1

N = int(input())
print(factorial(N))
