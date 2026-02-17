import sys

def solve():
    # 입력 받기
    n = int(sys.stdin.readline())
    
    # 수열 생성
    # A[1]=1, A[2]=2 그리고 A[3]부터 A[n-1]까지는 i를 그대로 사용 (3, 4, 5...)
    res = []
    for i in range(1, n):
        res.append(i)
    
    # 마지막 원소 A[n]은 소수여야 함
    # n의 최대값이 50이므로, 50보다 큰 소수인 997을 넣으면 무조건 성공!
    res.append(997)
    
    # 출력 형식 맞추기
    print(n)
    print(*(res))

if __name__ == "__main__":
    solve()