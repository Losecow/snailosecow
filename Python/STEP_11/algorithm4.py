# MenOfPassion(A[], n) {
#     sum <- 0;
#     for i <- 1 to n - 1
#         for j <- i + 1 to n
#             sum <- sum + A[i] × A[j]; # 코드1
#     return sum;
# }

N = int(input())

print(N * (N - 1) // 2)
print(2)

# 등차수열 일반항, 등차수열 합 공식