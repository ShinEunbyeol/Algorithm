import math

class Solution:
    def reverse(self, x: int) -> int:
        criterion = math.pow(2, 31)
        sign = -1 if x < 0 else 1
        xArr = [n for n in str(abs(x))][::-1]
        result = int(''.join(xArr))
        return result * sign if result <= criterion else 0