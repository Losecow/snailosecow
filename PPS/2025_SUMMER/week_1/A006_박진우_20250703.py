def solution(s):
    lowercase(s)
    answer = True
    answerP = [c for c in s if c == 'p']
    answerY = [c for c in s if c == 'y']
    
    if len(answerP) != len(answerY):
        answer = False
    

    return answer


def solution(s):
    s = s.lower()
    return s.count('p') == s.count('y')
