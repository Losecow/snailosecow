def solution(s):
    length = len(s)
    min_length = length

    for step in range(1, length // 2 + 1):
        compressed = ""
        prev = s[0:step]
        count = 1

        # 문자열을 step 단위씩 잘라서 순회
        for i in range(step, length, step):
            next_sub = s[i:i+step]
            
            # 이전 블록과 현재 블록이 같으면 count 증가
            if next_sub == prev:
                count += 1
            
            # 다르면 개수 + 문자로 추가
            else:
                compressed += (str(count) + prev) if count >= 2 else prev
                # 새 블록을 prev로 
                prev = next_sub
                count = 1
        
        # 마지막 처리
        compressed += (str(count) + prev) if count >= 2 else prev
        
        min_length = min(min_length, len(compressed))

    return min_length