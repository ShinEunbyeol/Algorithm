class Solution:
    def myAtoi(self, s: str) -> int:
        num = ""
        for i in range(len(s)):
            c = s[i]

            if c.isdigit() or (num == "" and (c == '-' or c == '+')):
                num += c
            elif c != " " or (c == " " and num != ""):
                break
        if num == "" or num == '-' or num == '+':
            num = "0"

        print(num)
        num = int(num)
        if num < -2**31:
            return -2**31
        if num > 2**31 - 1:
            return 2**31 - 1
        return num