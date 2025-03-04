def fibonacci(N):
    if N < 2:
        return N
    else:
        return fibonacci(N - 1) + fibonacci(N - 2)

N = int(input())
print(fibonacci(N))