class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n <= 0:
            return False
        while n % 4 == 0:
            n //= 4
        return n == 1

#----------------------------------------------------

class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        # 양수이고, 2의 거듭제곱이며, 4의 거듭제곱 위치에만 1이 있는 경우
        return n > 0 and (n & (n - 1)) == 0 and (n - 1) % 3 == 0
    
    
#----------------------------------------------------

import math
class Solution:
    def isPowerOfFour(self, n: int) -> bool:
        if n<=0:
            return False
        logval=math.log(n,4)
        return logval==int(logval)
