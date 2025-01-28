N = int(input())

user = []
for _ in range(N):
    age, name = input().split()
    user.append([int(age),name])

for age, name in sorted(user,key=lambda x : x[0]):
    print(age, name)
