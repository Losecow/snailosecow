import sys
input = sys.stdin.readline

N = int(input())

arrayList = list(map(int, input().split()))
arrayListSet = sorted(list(set(arrayList)))

# 정렬시키는 이유: 가장 작은 숫자는 자기보다 작은 숫자가 없으니 0일 테고... 이런 식으로 쭉 

# print(arrayList)
# print(arrayListSet)

# 시도 1. 딕셔너리 사용할 생각 하지못함, sorted도 생각못했음

# count = []

# for i in range(len(arrayList)):
#     cnt = 0
#     for j in range(len(arrayListSet)):
#         if arrayList[i] > arrayListSet[j]:
#             cnt += 1
#     count.append(cnt)

# print(*count)

# 찾아보다 알게된 index를 사용한 값 배정. 시간복잡도가 커서 이 문제에는 활용불가

# arr = list(map(int, input().split()))

# arr2 = sorted(list(set(arr)))

# for i in arr:
#     print(arr2.index(i), end = ' ')

# list.index(i) 형태의 시간 복잡도 = O(N) / 매번 최대 1,000,000번의 수행

# index[i] 형태의 시간 복잡도 = O(1)

dic = {arrayListSet[i] : i for i in range(len(arrayListSet))}

for i in arrayList:
    print(dic[i], end = ' ')