remain = [i for i in range(42)]

num = []
A = 0

while True:
    try:
        A = int(input())
        if A % 42 not in num:
            num.append(A % 42)
    except:
        break
    

print(len(num))
