# def factorial(N):
#     if N == 0:
#         return 1
#     elif N == 1:
#         return 1
#     else:
#         return N * factorial(N - 1)

def factorial(N):
    result = 1
    for i in range(2, N + 1):
        result *= i
    return result

N = int(input())

quotient = N // 2
remainder = N % 2
cnt = 0

# print(quotient, remainder)

if remainder == 1:
    cnt += 1
    while quotient > 0:
        cnt += factorial(quotient + remainder) // (factorial(quotient) * factorial(remainder))
        quotient -= 1
        remainder += 2
        # print(quotient, remainder)

elif remainder == 0:
    while quotient >= 0:
        cnt += factorial(quotient + remainder) // (factorial(quotient) * factorial(remainder))
        # print(quotient, remainder, cnt)
        quotient -= 1
        remainder += 2
        # print(quotient, remainder, cnt)

print(cnt % 10007)