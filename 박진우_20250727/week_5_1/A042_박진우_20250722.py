class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        def build(string):
            stack = []
            for ch in string:
                if ch == '#':
                    if stack:
                        stack.pop()
                else:
                    stack.append(ch)
            return ''.join(stack)

        return build(s) == build(t)

#----------------------------------------------


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        stack_s=[]
        stack_t=[]

        for c in s :

            if stack_s and c == "#":
                stack_s.pop()
            elif len(stack_s) == 0 and c == "#" :
                continue
            else:
                stack_s.append(c)

        for  i in t:
            if stack_t and i == "#":
                stack_t.pop()
            elif len(stack_t) == 0 and i == "#" :
                continue
            else:
                stack_t.append(i)

        
        return stack_s == stack_t