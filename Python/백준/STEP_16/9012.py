N = int(input())

for i in range(N):
    x = input()
    ps_stack = []

    for j in x:
        if j == "(":
            ps_stack.append("(")
        else:
            if len(ps_stack) == 0:
                ps_stack.append(")")
                break
            else:
                ps_stack.pop()

    if len(ps_stack) != 0:
        print('NO')
    else:
        print('YES')