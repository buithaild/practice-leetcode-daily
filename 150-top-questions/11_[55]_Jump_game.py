"""
You are given a 0-indexed array of integers nums of length n. You are initially positioned at index 0.

Each element nums[i] represents the maximum length of a forward jump from index i. In other words, if you are at index i, you can jump to any index (i + j) where:

0 <= j <= nums[i] and
i + j < n
Return the minimum number of jumps to reach index n - 1. The test cases are generated such that you can reach index n - 1.



Example 1:

Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.
Example 2:

Input: nums = [2,3,0,1,4]
Output: 2
"""

from typing import List
class Solution:
    def canJump2(self, nums: List[int]) -> int:
        n = len(nums)
        smallest = 0
        end, far = 0, 0
        for i in range(n-1):
            far = max (far, i + nums[i])

            if i == end:
                smallest += 1
                end = far
        return smallest
if __name__ == '__main__':
    s = Solution()
    nums = [2,3,1,1,4]
    res = s.canJump2(nums)
    print(res)
