N = int(input()) 

# 중복을 제거하기 위한 set 사용
listWord = set()  

for i in range(N):
    word = input()

# set에 단어 추가 (중복 자동 제거)
    listWord.add(word)  


wordLength = [(word, len(word)) for word in listWord]


sortedWords = sorted(wordLength, key=lambda x: (x[1], x[0]))


for word, length in sortedWords:
    print(word)

# for word, length in sortedWords: 부분은 **언패킹(unpacking)**을 사용하는 코드입니다. 
# sortedWords 리스트에는 (단어, 길이) 형태의 튜플들이 저장되어 있기 때문에, 
# 각 튜플에서 단어와 길이를 분리하여 word와 length라는 변수에 각각 할당하는 방식입니다.

