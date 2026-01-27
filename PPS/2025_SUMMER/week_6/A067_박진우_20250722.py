class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for c in s:
            if stack and stack[-1] == c:
                stack.pop()
            else:
                stack.append(c)
        return ''.join(stack)
        
        
 #-----------------------------------------------
 
 
 class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack=[]
        
        for i in s:
            if stack and stack[-1] == i:
                stack.pop()
            else:
                stack.append(i)  

                  
        return "".join(stack) 