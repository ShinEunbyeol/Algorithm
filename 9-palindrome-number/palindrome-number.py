class Solution:
    def isPalindrome(self, x: int) -> bool:
        x_str = str(x)
        return True if x_str == x_str[::-1] else False