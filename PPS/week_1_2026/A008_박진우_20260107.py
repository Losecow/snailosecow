n = int(input())

for _ in range(n):
    s = list(map(int, input().split()))
    m = sum(s[1:]) / s[0]
    avr = [c for c in s[1:] if c > m]
    rate = len(avr) / s[0] * 100
    print(f"{rate:.3f}%")
