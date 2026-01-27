class Solution:
    def isPalindrome(self, s: str) -> bool:
        filtered = [c.lower() for c in s if c.isalnum()]
        return filtered == filtered[::-1]



#---------------------------


class Solution:
    def isPalindrome(self, s: str) -> bool:
        res = []
        for i in s.lower():
            if i.isalnum():
                res.append(i)
        return res == res[::-1]