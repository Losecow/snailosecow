class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        num = int("".join(map(str, digits)))
        num += 1
        return [int(c) for c in str(num)]

result = [int(c) for c in "124"]
