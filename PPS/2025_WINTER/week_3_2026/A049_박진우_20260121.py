def is_acceptable(pw):
    vowels = "aeiou"
    
    has_vowel = False
    vowel_cnt = 0
    consonant_cnt = 0

    for i in range(len(pw)):
        ch = pw[i]
        
        # 모음 체크
        if ch in vowels:
            has_vowel = True
            vowel_cnt += 1
            consonant_cnt = 0
        else:
            consonant_cnt += 1
            vowel_cnt = 0
        
        # 모음/자음 3개 연속 체크
        if vowel_cnt == 3 or consonant_cnt == 3:
            return False
        
        # 같은 글자 두 번 연속 (ee, oo는 예외)
        if i > 0 and pw[i] == pw[i-1] and pw[i] not in "eo":
            return False

    return has_vowel

# 입력 처리
while True:
    word = input()
    if word == "end":
        break
    if is_acceptable(word):
        print(f"<{word}> is acceptable.")
    else:
        print(f"<{word}> is not acceptable.")
