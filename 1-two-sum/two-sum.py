class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        cnt = len(nums)
        for i in range(cnt-1):
            num_i = nums[i]
            for j in range(i+1, cnt):
                num_j = nums[j]
                if num_i + num_j == target:
                    return [i, j]
        return []