# Given an integer array nums, return true if any value appears at least twice in the array,
# and return false if every element is distinct.
from typing import List


class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        # #Cach 1
        # nums.sort()
        # for i in range(1, len(nums)):
        #     if (nums[i] - nums[i-1] == 0):
        #         return True
        #     return False

        #Cach 2
        #Set không chứa element trùng lặp
        if (len(set(nums)) == len(nums)):
            return False
        else:
            return True

if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,4,1]
    res = solution.containsDuplicate(nums)
    print(res)
    print("Test set: ", set(nums))




