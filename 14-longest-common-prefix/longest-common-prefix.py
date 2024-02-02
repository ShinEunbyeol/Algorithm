class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(set(strs)) == 0 or len(strs) <= 1:
            return strs[0]

        shortStr = min(strs, key=len)
        for i, c in enumerate(shortStr):
            for otherStr in strs:
                if otherStr[i] != c:
                    return shortStr[:i]
        
        return shortStr