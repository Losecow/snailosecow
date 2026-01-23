import sys
input = sys.stdin.readline

n = int(input())

num = set()    
calculation = ""

for i in range(n):

    calculation = input().split()

    if calculation[0] == "add":
        if int(calculation[1]) in num:
            continue
        else:
            num.add(int(calculation[1]))
    
    elif calculation[0] == "remove":
        if int(calculation[1]) in num:
            num.remove(int(calculation[1]))

    elif calculation[0] == "check":
        if int(calculation[1]) in num:
            print("1")
        else:
            print("0")
    
    elif calculation[0] == "toggle":
        if int(calculation[1]) in num:
            num.remove(int(calculation[1]))
        else:
            num.add(int(calculation[1]))
    
    elif calculation[0] == "all":
        # for i in range(1, 21):
        #     if i not in num:
        #         num.add(i)
        #     else:
        #         continue
        num = set(range(1, 21))


    elif calculation[0] == "empty":
        # for _ in range(len(num)):
        #     num.pop()
        num.clear()
