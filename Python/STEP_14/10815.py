import sys
input = sys.stdin.readline

N = int(input())
A = list(map(int, input().split()))

M = int(input())
B = list(map(int, input().split()))

A.sort()

A_dict = {} 

for i in range(len(A)):
    A_dict[A[i]] = 0 

for j in range(M):
    if B[j] not in A_dict:
        print(0, end=' ')
    else:
        print(1, end=' ')