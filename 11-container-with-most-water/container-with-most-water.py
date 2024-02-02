class Solution:
    def maxArea(self, height: List[int]) -> int:
        # 힌트 확인: 양끝에서 시작
        leftIdx = 0
        rightIdx = len(height) - 1
        mostArea = 0
        while leftIdx < rightIdx:
            area = (rightIdx - leftIdx) * min([height[leftIdx], height[rightIdx]])
            if area > mostArea:
                mostArea = area
            
            if height[leftIdx] > height[rightIdx]:
                rightIdx -= 1
            else:
                leftIdx += 1
        return mostArea