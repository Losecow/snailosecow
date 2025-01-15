A, B, C = map(int, input().split())

if A == B:
    if A == C:
        print(A * 1000 + 10000) # 셋 다 같은 경우
    else:
        print(A * 100 + 1000) # A, B 만 같은 경우
elif A != B:
    if A == C:
        print(A * 100 + 1000) # A, C 만 같은 경우
    elif C == B:
        print(B * 100 + 1000) # B, C 만 같은 경우
    elif A != C:
        if A > B and A > C:
            print(A * 100)
        elif B > A and B > C:
            print(B * 100)
        elif C > A and C > B:
            print(C * 100)

        
