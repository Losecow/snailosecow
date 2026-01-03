n = int(input())

stack = []
answer = []
count = 1
temp = True

for i in range(n):
    m = int(input())

    while count <= m:
        stack.append(count)
        answer.append("+")
        count += 1
    
    if stack[-1] == m:
        stack.pop()
        answer.append("-")
    
    else:
        temp = False
        break

if temp == False:
    print("No")
else:
    for i in answer:
        print(i)
         

    
    