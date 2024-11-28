N = int(input())
M = int(input())

if N > 0:
    if M > 0:
        print("1")
    else:
        print("4")
elif N < 0:
    if M > 0:
        print("2")
    else:
        print("3")
