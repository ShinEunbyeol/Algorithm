class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1 or numRows >= len(s):
            return s

        position = ['' for i in range(numRows)]
        currRow = 0
        direction = 1
        for c in s:
            position[currRow] += c

            if currRow >= numRows-1:
                direction = -1
            elif currRow == 0:
                direction = 1
                
            currRow = currRow + direction * 1

        return "".join(position)