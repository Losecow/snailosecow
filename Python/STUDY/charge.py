# 춘향이는 편의점 카운터에서 일한다.

# 손님이 2원짜리와 5원짜리로만 거스름돈을 달라고 한다. 2원짜리 동전과 5원짜리 동전은 무한정 많이 가지고 있다. 동전의 개수가 최소가 되도록 거슬러 주어야 한다. 거스름돈이 n인 경우, 최소 동전의 개수가 몇 개인지 알려주는 프로그램을 작성하시오.

# 예를 들어, 거스름돈이 15원이면 5원짜리 3개를, 거스름돈이 14원이면 5원짜리 2개와 2원짜리 2개로 총 4개를, 거스름돈이 13원이면 5원짜리 1개와 2원짜리 4개로 총 5개를 주어야 동전의 개수가 최소가 된다.

# N = int(input())

# five_quotient = N / 5
# five_remainder = N % 5

# two_quotient = 0
# two_remainder = 0


# if five_remainder / 2 == 0:
#     print(five_quotient + five_remainder / 2)
# elif five_remainder / 2 != 0:
#     while True:
#         (N / 5) 
# 망코


# 18 -> 
# 17 -> 15 + 2
# 16 -> 15 + 1 x
# -> 16 -> 2 * 8
# 15
# 14 -> 10 + 4
# 13 -> 5 + 8


N = int(input())

five = 0
count5 = 0

while True:
    if N == 3 or N == 1:
        print(-1)
        break
    if ((N % 5) + five) % 2 == 0:
        print(int((N // 5) - count5 + ((N % 5) + 5 * count5) / 2))
        break
    elif ((N % 5) + five) % 2 != 0:
        five += 5
        count5 += 1
    else:
        print(-1)