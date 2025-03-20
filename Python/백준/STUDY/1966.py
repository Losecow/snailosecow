from collections import deque
import sys

testCase = int(input())

for i in range(testCase):
    N, M = map(int, input().split())
    queue = deque(list(map(int, sys.stdin.readline().split())))
    count = 0
    while queue:
        best = max(queue)  
        front = queue.popleft()
        M -= 1 

        if best == front: 
            count += 1 
            if M < 0: 
                print(count)
                break

        else:   
            queue.append(front) 
            if M < 0 :  
                M = len(queue) - 1 


# 내가 짠 쓰레기코드
# 내일다시보자

# testCase = int(input())

# for _ in range(testCase):
#     N, M = map(int, input().split())
#     printPriority = list(map(int, input().split()))
#     printQueue = {}
#     answer = []
    
#     for i in range(N):
#         printQueue[printPriority[i]] = i

#     for i in range(N - 1):
#         if printPriority[i] <= printPriority[i + 1]:
#             key, value = printQueue.popitem()
#             printQueue[key] = value
#         else:
#             key, value = printQueue.popitem()
#             if value == M:
#                 answer.append(key)
#                 break


# print(answer)
