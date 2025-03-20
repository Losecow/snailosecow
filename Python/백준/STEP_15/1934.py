def GCD(a, b): # 최대공약수
    while b > 0:
        a, b = b, a % b
    return a

def LCM(a, b): # 최소공배수 (두 수의 곱을 최대공약수로 나눈 값)
    return a * b / GCD(a, b)

N = int(input())

for _ in range(N):
    A, B = map(int, input().split())
    print(int(LCM(A, B)))
