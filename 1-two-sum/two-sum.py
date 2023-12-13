class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt = len(nums)
        for i in range(cnt-1):
            for j in range(i+1, cnt):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []