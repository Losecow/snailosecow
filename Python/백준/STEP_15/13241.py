import sys
input = sys.stdin.readline

def GCD(a, b): # Greatest Common Divisor
    while b > 0:
        a, b = b, a % b
    return a

def LCM(a, b): # Least Common Multiple / Lowest Common Multiple
    return a * b / GCD(a, b)

A, B = map(int, input().split())
print(int(LCM(A, B)))