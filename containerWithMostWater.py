from typing import List
class Solution:
    def maxArea(self, height: List[int]) -> int:
        maxArea = 0
        left = 0
        right = len(height) - 1

        while left < right:
            chieuRong = min(height[left], height[right])
            chieuDai = right - left

            maxArea = max(maxArea, chieuDai*chieuRong)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1
        return maxArea
if __name__ == "__main__":
    solution = Solution()
    num = [1,8,6,2,5,4,8,3,7]
    result = solution.maxArea(num)
    print(result)