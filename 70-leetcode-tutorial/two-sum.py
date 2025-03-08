# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
#
# You can return the answer in any order.
from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hash_map = {} #val, idx

        for idx, val in enumerate(nums):
            diff = target - val
            print("diff: ", diff)
            if diff in hash_map:
                return [hash_map[diff], idx]
            hash_map[val] = idx
            print("hash: ", hash_map)


if __name__ == "__main__":
    s = Solution()
    nums = [2,11,7,5]
    target = 9
    res = s.twoSum(nums, target)
    print(res)

