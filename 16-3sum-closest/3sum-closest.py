class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # target에 가장 가까운 숫자 3개의 합 리턴
        # 각 입력에는 정확히 하나의 솔루션이 있다고 가정

        nums.sort()
        numsCnt = len(nums)
        result = 0
        prev = nums[0] - 1
        for i in range(numsCnt - 2):
            if prev == nums[i]:
                continue
            prev = nums[i]

            j = i + 1
            k = numsCnt - 1
            while j < k:
                currSum = nums[i] + nums[j] + nums[k]
                currGap = abs(target + (currSum * -1))
                if currGap == 0:
                    return currSum
                elif 'minGap' not in locals() or currGap <= minGap:
                    result = currSum
                    minGap = currGap
                
                if currSum < target:
                    j += 1
                else:
                    k -= 1
        return result