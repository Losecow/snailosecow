# a + 3b + c + 3d ... 12번째 + 13번째 // 10 = 나머지가 0
# (~~~) + 13 나누기 10 했을 때 나머지가 없는거니까
# 13 은 0~9 사이의 수
# 12 까지의 수 다 더한다음에 13 더하고 나누기 나머지가 0일 때 만족
# 중간에 하나 숫자가 비었을 때 0으로 바꿔치기 한다면?
# (~~~) 이거 + 13번째 수가 10으로 나누어 떨어지지 않을거임
# 그렇다면 ... 짝수일 경우 *3 , 홀수면 그냥
# 예를 들어 결과가 123 이 나옴 그럼 13은 7일거임
# 근데 하나가 빠지면 (~~~) 이렇게 나올거고 13은 여전히 7임
# ? - 13번 수 = ? - 13
# ? - 13 // 10 은 
# 
# 1 2 3 4 5 6 7 8 9 10 11 12 13
# 3 1 3 1 3 1 3 1 3 1  3  1 
# 36 이니까 13은 4
# 2를 비워보면  
# 1 2 3 4 5 6 7 8 9 10 11 12 13
# 3 0 3 1 3 1 3 1 3 1  3  1 
# 33, 13은 4
# 37
# 37 % 10은 7 남음
# 10 - 7 = 3
# 짝수니까 % 3 해줘야함
# 2 -> 1

# 0으로 치환해서 더한 뒤 나눴을 때 나머지를 구하고
# 10에서 나머지를 뺀 다음
# 나누기 3을 하면 빈 수의 값이 나옴

# n = input()

# ISBN = list(n)
# sum = 0
# num = 0
# p = 0
# for i in range(0, 12):
#     if ISBN[i] == "*":
#         ISBN[i] = 0
#         p = i + 1
        
#     if i % 2 == 0:
#         num = 1
#     else:
#         num = 3
       
#     sum += int(ISBN[i]) * num
    
# if sum % 10 == 0 and int(ISBN[12]) == 0:
#     print("0")
# else:
#     # print("sum=", sum)
#     # print("13 = ",ISBN[12])
#     # print("p= ", p)
#     # print("(sum + int(ISBN[12])) % 10)", (sum + int(ISBN[12])) % 10)
#     if p % 2 == 0:
#         print((10 - ((sum + int(ISBN[12])) % 10)) // 3)
#     else:
#         print((10 - ((sum + int(ISBN[12])) % 10)))


n = input()
ISBN = list(n)

total = 0
pos = 0

for i in range(13):
    if ISBN[i] == '*':
        pos = i
        continue

    if i % 2 == 0:
        total += int(ISBN[i])
    else:
        total += 3 * int(ISBN[i])

# total = 알려진 숫자들의 가중합
# x가 들어갈 자리의 가중치
weight = 1 if pos % 2 == 0 else 3

m = total % 10
need = (10 - m) % 10

if weight == 1:
    print(need)
else:
    print((need * 7) % 10)


#시도는 좋았다.


