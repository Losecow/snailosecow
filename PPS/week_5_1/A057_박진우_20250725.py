def solution(cookie):
    n = len(cookie)
    answer = 0
    
    for m in range(n-1):
        l = m
        r = m + 1
        left = cookie[l]
        right = cookie[r]
        while l >= 0 and r < n:
            if left == right:
                answer = max(answer, left)
                l -= 1
                if l >= 0:
                    left += cookie[l]
            elif left < right:
                l -= 1
                if l >= 0:
                    left += cookie[l]
            else:
                r += 1
                if r < n:
                    right += cookie[r]
        
    return answer
    
    
    #--------------------------------
    
    

from itertools import accumulate

def solution(cookie):
    answer = 0
    for m in range(len(cookie)-1):
        a = set(accumulate(reversed(cookie[:m+1])))
        b = set(accumulate(cookie[m+1:]))
        c = a & b

        if c:
            answer = max(*c, answer)
    return answer