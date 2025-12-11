"""
Given an array nums of size n, return the majority element.

The majority element is the element that appears more than ⌊n / 2⌋ times. You may assume that the majority element always exists in the array.



Example 1:

Input: nums = [3,2,3]
Output: 3
Example 2:

Input: nums = [2,2,1,1,1,2,2]
Output: 2
"""

from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> int:

        # ### CACH 1: HASH MAP
        # hash_map = {}
        # for num in nums:
        #     if num in hash_map:
        #         hash_map[num] += 1
        #     else:
        #         hash_map[num] = 1
        #
        # max_count = -1
        # ans = -1
        #
        # for key, value in hash_map.items():
        #     if value > max_count:
        #         max_count = value
        #         ans = key
        # return ans
        # #Time O(n)
        # #Space O(n)


        # ### CACH 2:
        ans = -1
        count = 0

        for num in nums:
            if count == 0:
                ans = num
            if ans == num:
                count += 1
            else:
                count -= 1
        return ans
        #Time O(n)
        #Space O(1)

if __name__ == "__main__":
    s = Solution()
    nums = [2,2,1,1,1,2,2]
    res = s.majorityElement(nums)
    print(res)