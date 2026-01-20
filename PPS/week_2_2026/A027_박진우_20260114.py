def solution(number, k):
    stack = []
    for num in number:
        while stack and k > 0 and stack[-1] < num:
            stack.pop()
            k -= 1
        stack.append(num)
    
    # 아직 제거 안 한 숫자가 남았으면 뒤에서 자름
    if k > 0:
        stack = stack[:-k]
    
    return ''.join(stack)
