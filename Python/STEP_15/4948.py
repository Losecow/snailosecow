def primeNum(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

while True:
    n = int(input())
    
    if n == 0:
        break
    
    prime = 0
    for i in range(n + 1, 2 * n + 1):
        if primeNum(i):
            prime += 1
    print(prime)