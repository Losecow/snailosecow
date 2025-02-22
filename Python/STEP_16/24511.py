from collections import deque
import sys
input = sys.stdin.readline

N = int(input())                    # queuestack을 구성하는 N개의 자료구조
A = list(map(int, input().split())) # 길이 N의 수열 A
B = list(map(int, input().split())) # 길이 N의 수열 B
M = int(input())                    # 삽입할 수열의 길이 M
C = list(map(int, input().split())) # 길이 M의 수열 C

queue = deque([])
for i in range(N):
    if A[i] == 0: # 큐인 자료구조만 모으기
        queue.append(B[i])

# 배열 C의 원소를 1개 appendleft 할 때마다 pop 연산 수행
for i in range(M):
    queue.appendleft(C[i])
    print(queue.pop(), end= ' ')

# https://dduniverse.tistory.com/entry/%EB%B0%B1%EC%A4%80-24511-queuestack-%ED%8C%8C%EC%9D%B4%EC%8D%AC-python