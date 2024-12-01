A,B = input().split()

print(int(A) + int(B))
print(int(A) - int(B))
print(int(A) * int(B))
print(int(int(A) / int(B)))
print(int(A) % int(B))

# 처음 문제를 읽고 제출했을 때 오답이 나왔다
# 문제는 문제의 의도대로는 풀었지만 나누기 부분에서 몫만 구했어야 했는데, 소숫점 자리까지 표현한 것이 문제였다
# 앞으로는 문제를 풀 때 예시의 결과까지 참고해서 코드를 다듬어야 한다.
