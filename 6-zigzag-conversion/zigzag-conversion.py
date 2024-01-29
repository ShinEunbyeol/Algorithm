class Solution:
    def convert(self, s: str, numRows: int) -> str:
        if numRows == 1:
            return s
            
        result = ""
        position = [["" for j in range(len(s))] for i in range(numRows)]
        numCols = 0
        idx = 0
        for x in range(len(s)):
            if numCols % 2 == 0:
                for r in range(numRows):
                    if idx < len(s):
                        position[r][numCols] = s[idx]
                        idx += 1
            else:
                for r in range(numRows-2, 0, -1):
                    if idx < len(s):
                        position[r][numCols] = s[idx]
                        idx += 1

            if idx >= len(s):
                break
            numCols += 1

        for x in range(len(position)):
            result += "".join(position[x])

        return result