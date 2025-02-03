import sys
input = sys.stdin.readline

N, M = map(int, input().split())
A = list(map(int, input().split()))
B = list(map(int, input().split()))

A = {value: 0 for value in A}
B = {value: 0 for value in B}

cnt = 0

for key, value in A.items():
    if key in B:
        A[key] += 1

for key, value in B.items():
    if key in A:
        B[key] += 1

for key, value in A.items():
    if value == 0:
        cnt += 1

for key, value in B.items():
    if value == 0:
        cnt += 1

print(cnt)

# 집합 이라는 개념 새로 알았음

# n,m=map(int,input().split())
# a=list(map(int,input().split()))
# s1=set(a)
# b=list(map(int,input().split()))
# s2=set(b)
# s3=s1-s2 # 차집합
# s4=s2-s1
# s5=s3|s4 # 합집합 // & -> 교집합
# print(len(s5))

# set -> 집합 