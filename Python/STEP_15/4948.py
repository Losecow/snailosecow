import sys
input = sys.stdin.readline

def primeNum(x):
    if x == 1:
        return False
    else:
        for i in range(2, int(x ** 0.5) + 1):
            if x % i == 0:
                return False
        return True

numList = list(range(2, 246912)) 
primNumList = []

for i in numList:
    if primeNum(i):
        primNumList.append(i) 

n = int(input()) 

while True:
    cnt = 0 
    if n == 0: 
        break
    for i in primNumList:
        if n < i <= 2 * n:
            cnt += 1
    print(cnt)
    n = int(input()) 