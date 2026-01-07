def fib(n):
    if n == 1 or n == 2:
        return 1  # 코드1
    else:
        return fib(n - 1) + fib(n - 2)
    

def fibonacci(n):   
    if n == 1 or n == 2:
        return 1

    f = [0] * (n + 1)

    f[1] = 1
    f[2] = 1

    count = 0
    for i in range(3, n + 1):
        f[i] = f[i - 1] + f[i - 2]  # 코드2
        count += 1

    return count


n = int(input())
print(fib(n), fibonacci(n))