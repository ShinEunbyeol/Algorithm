import math

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergeList = nums1 + nums2
        mergeList.sort()
        cnt = len(mergeList)

        nextIdx = math.ceil(cnt/2)
        centerIdx = nextIdx - 1
        return float(mergeList[centerIdx]) if cnt % 2 == 1 else (mergeList[centerIdx] + mergeList[nextIdx]) / 2