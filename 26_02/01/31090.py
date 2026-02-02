Test = int(input())
 
for _ in range(Test):
    N = int(input())

    if (N + 1) % int(str(N)[2:]) == 0:
        print("Good")
    else:
        print("Bye")