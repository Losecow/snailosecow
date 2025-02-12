import sys
input = sys.stdin.readline

primeNum = list(True for _ in range(1000001))
primeNum[0] = False
primeNum[1] = False

for i in range(2, 1000001):
    if primeNum[i]:
        for j in range(i * 2, 1000001, i): # i * 2 부터 1000001 까지, i 값이 증가
            primeNum[j] = False # i의 배수를 지워주는 과정이다 (에라토스테네스의 체)
        
N = int(input())

for _ in range(N):
    temp = int(input()) # 주어지는 수
    count = 0 # 파티션 갯수 카운트
    for i in range(2, temp // 2 + 1): # 중복되는 파티션의 갯수를 막기 위해 temp의 절반값+1을 사용
        if (primeNum[i] and primeNum[temp - i]):
# 간단히 설명
# ex) 10의 골드바흐 파티션을 구한다고 치자
# 10보다 작은 소수는 2 3 5 7
# 2부터 시작한다고 할 때, pirmeNum[2] = 2 , primeNum[10 - 2] = 8(false) and 조건 불만족
# 3일때 -> primeNum[3] = 3 , primeNum[10 - 3] = 7(true) and 조건 만족
# 임의의 수에서 소수를 감하였을 때, 값이 소수라면 count를 늘리는 방식
            count += 1
            
    print(count)
