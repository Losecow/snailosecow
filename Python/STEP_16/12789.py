N = int(input())

numberTickets = list(map(int, input().split())) 

stack = []

objective = 1
for people in numberTickets:
    stack.append(people)
    while stack and stack[-1] == objective:
        stack.pop() 
        objective +=1

if stack: 
    print('Sad') 
else:
    print('Nice')

# https://chaeyami.tistory.com/177