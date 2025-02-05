def GCD(a, b):
    while b > 0:
        a, b = b, a % b
    return a

def LCM(a, b):
    return a * b / GCD(a, b)

N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    print(int(LCM(A, B)))
