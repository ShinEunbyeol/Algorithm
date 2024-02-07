class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        # 힌트 확인: nums 오름차순 정렬 후 중심값 기준으로 나머지 2개의 인덱스 증감
        if len(nums) == 3 and sum(nums) == 0:
            return [nums]

        nums.sort()
        numsCnt = len(nums)
        result = set()
        for i in range(numsCnt-2):
            j = i + 1
            k = numsCnt - 1
            while j < k:
                currSum = nums[i] + nums[j] + nums[k]
                if currSum == 0:
                    result.add((nums[i], nums[j], nums[k]))
                    j += 1
                elif currSum > 0:
                    k -= 1
                else:
                    j += 1
        return result
        