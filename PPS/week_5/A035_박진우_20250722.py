T = int(input())
for _ in range(T):
    tokens = input().split()
    val = float(tokens[0])
    for op in tokens[1:]:
        if op == '@': val *= 3
        elif op == '%': val += 5
        elif op == '#': val -= 7
    print(f"{val:.2f}")