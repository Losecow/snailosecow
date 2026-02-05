import sys

# 1. 후보자의 수 N 입력
n = int(sys.stdin.readline())

# 2. 3글자인 후보자들을 담을 리스트 생성
candidates = []

for _ in range(n):
    name = sys.stdin.readline().strip()
    
    # 3. 이름의 길이가 정확히 3인 경우만 리스트에 추가
    if len(name) == 3:
        candidates.append(name)

# 4. 사전 순으로 정렬 (A-Z 순서)
candidates.sort()

# 5. 가장 앞선 이름 출력
print(candidates[0])