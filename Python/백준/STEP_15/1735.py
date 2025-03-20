import math

A1, A2 = map(int, input().split())
B1, B2 = map(int, input().split())

C = math.lcm(A2, B2) # 분모 denominator
D = (C // A2 * A1) + (C // B2 * B1) # 분자 numerator

E = math.gcd(C, D)

print(D // E, C // E)