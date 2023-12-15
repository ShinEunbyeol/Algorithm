import numpy as np

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        mergeList = nums1 + nums2
        mergeList.sort()
        return np.median(mergeList)