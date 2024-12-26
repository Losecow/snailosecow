N, B = map(int, input().split())
S = ''

N_list = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

while N:
    S += str(N_list[N % B]) # 글자를 하나씩 문자열에 추가
    N //= B # B 로 나눈 몫을 저장

print(S[::-1])