"""
Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.



Example 1:

Input: nums = [1,2,3,4,5,6,7], k = 3
Output: [5,6,7,1,2,3,4]
Explanation:
rotate 1 steps to the right: [7,1,2,3,4,5,6]
rotate 2 steps to the right: [6,7,1,2,3,4,5]
rotate 3 steps to the right: [5,6,7,1,2,3,4]
Example 2:

Input: nums = [-1,-100,3,99], k = 2
Output: [3,99,-1,-100]
Explanation:
rotate 1 steps to the right: [99,-1,-100,3]
rotate 2 steps to the right: [3,99,-1,-100]
"""

from typing import List

class Solution:
    def roatedArray189(self, nums: List[int], k: int) -> None:
        ### CACH 1
        n = len(nums)
        k = k % n
        roated = [0] * n

        for i in range(n):
            roated[(i+k)%n] = nums[i]

        for i in range(n):
            nums[i] = roated[i]

        return nums

        # # ### CACH 2
        #
        # n = len(nums)
        # k = k%n
        #
        # def reserve(left, right):
        #     while left < right:
        #         nums[left], nums[right] = nums[right], nums[left]
        #         left += 1
        #         right -= 1
        # ## step 1: reserve the whole array
        # reserve(0, n-1)
        # ## step 2: reserve the first k elements
        # reserve(0, k-1)
        # ## step 3: reserve the rest n-k elements
        # reserve(k, n-1)
        # return nums


if __name__ == '__main__':
    s = Solution()
    nums = [1,2,3,4,5,6,7]
    k = 3
    res = s.roatedArray189(nums, k)
    print(res)