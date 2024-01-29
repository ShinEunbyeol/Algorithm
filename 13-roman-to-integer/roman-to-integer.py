class Solution(object):
    def romanToInt(self, s):
        romanNum_dict = {'I': 1, 'V': 5, 'X': 10, 'L': 50, 'C': 100, 'D': 500, 'M': 1000}
        beforeC = ""
        num = 0
        for c in s[::-1]:
            sign = 1
            if (c == "I" and (beforeC == "V" or beforeC == "X")) or (c == "X" and (beforeC == "L" or beforeC == "C")) or (c == "C" and (beforeC == "D" or beforeC == "M")):
                sign = -1
            beforeC = c

            num += sign * romanNum_dict[c]

        return num