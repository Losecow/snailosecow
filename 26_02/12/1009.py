import sys
input = sys.stdin.readline
# 테스트 케이스 개수 입력
t = int(input())

for _ in range(t):
    a, b = map(int, input().split())
    
    # 밑인 a를 10으로 나눈 나머지로 단순화
    base = a % 10
    
    # 밑이 10의 배수인 경우 (일의 자리가 0)
    if base == 0:
        print(10)
    else:
        # 지수 b를 4의 배수 주기로 계산
        # (b % 4가 0일 때를 대비해 (b-1) % 4 + 1 식을 사용하거나 예외 처리)
        exp = (b - 1) % 4 + 1
        result = (base ** exp) % 10
        print(result)