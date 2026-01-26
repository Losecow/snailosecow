# 문자열 입력 받기
music = input().strip()

# 마디별로 나누기
parts = music.split("|")

# 가단조(A-minor)와 다장조(C-major)에 속하는 음들
aminor = ['A', 'D', 'E']
cmajor = ['C', 'F', 'G']

# 센 값 초기화
cnt_aminor = 0
cnt_cmajor = 0

# 각 마디의 맨 앞 음 체크
for p in parts:
    if len(p) == 0:
        continue
    first = p[0]
    if first in aminor:
        cnt_aminor += 1
    if first in cmajor:
        cnt_cmajor += 1

# 같을 때는 마지막 음으로 결정
if cnt_aminor == cnt_cmajor:
    last = music[-1]
    if last in aminor:
        cnt_aminor += 1
    if last in cmajor:
        cnt_cmajor += 1

# 결과 출력
if cnt_aminor > cnt_cmajor:
    print("A-minor")
else:
    print("C-major")
