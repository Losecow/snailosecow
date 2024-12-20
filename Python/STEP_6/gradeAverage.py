rating = ['A+', 'A0', 'B+', 'B0', 'C+', 'C0', 'D+', 'D0', 'F']
grade = [4.5, 4.0, 3.5, 3.0, 2.5, 2.0, 1.5, 1.0, 0]

total = 0	# 학점 총합을 담을 변수
result = 0	# (학점 * 과목평점) 총합을 담을 변수
for _ in range(20) :
    s, p, g = input().split()
    p = float(p)
    if g != 'P' :	# 등급이 P인 과목은 계산 안함
        total += p
        result += p * grade[rating.index(g)]

print('%.6f' % (result / total))


# 내코드

A_grade = ["F", "D0", "D+", "C0", "C+", "B0", "B+", "A0", "A+"]
grade = []

sum_Grade = 0
sum_GradeCount = 0

while True:
    try:
        A, B, C = input().split()
        if C != "P":
            for i in range(len(A_grade)):
                if C == A_grade[i]:
                    sum_GradeCount += float(B)
                    if i == 0:
                        break
                    else:
                        sum_Grade += float(B) * ((i / 2) + 0.5)
    except:
        break
        
print(sum_Grade / sum_GradeCount)
