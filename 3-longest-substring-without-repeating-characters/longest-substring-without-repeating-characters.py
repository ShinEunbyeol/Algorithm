class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        findStr = []
        cnt = 0
        for c in s:
            if c in findStr:
                idx = findStr.index(c)
                findStr = findStr[idx+1:strCnt]
            findStr.append(c)
            strCnt = len(findStr)

            cnt = strCnt if cnt < strCnt else cnt
        return cnt