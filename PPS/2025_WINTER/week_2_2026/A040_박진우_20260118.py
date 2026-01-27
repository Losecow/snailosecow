class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = set('aeiouAEIOU')
        mid = len(s) // 2
        a = s[:mid]
        b = s[mid:]
        
        count_a = sum(1 for c in a if c in vowels)
        count_b = sum(1 for c in b if c in vowels)
        
        return count_a == count_b

#------------------------------------------------------

class Solution:
    def halvesAreAlike(self, s: str) -> bool:
        vowels = ['a','e','i','o','u']
        lower = s[:len(s)//2].lower()
        upper = s[len(s)//2:].lower()
        l_count = 0
        u_count = 0
        for v in vowels:
            l_count += lower.count(v)
            u_count += upper.count(v)
        return l_count==u_count