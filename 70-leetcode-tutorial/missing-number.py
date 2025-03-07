# Given an array nums containing n distinct numbers in the range [0, n], return the only number
# in the range that is missing from the array.
from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        # #Cach 1
        # ####ADD
        # # # Case [1,2,3] thi tr ve 0
        # # if nums[0] != 0:
        # #     return 0
        # # nums.sort()
        # # #Case [0,1,2] thi tra ve 3
        # # if nums[-1] != len(nums):
        # #     return len(nums)
        #
        # for i in range(1, len(nums)):
        #     if (nums[i] - nums[i-1] == 2):
        #         return nums[i] - 1
        # return -1

        # Cach 2:
        # nums.sort()
        # for i, val in enumerate(nums):
        #     if( i != val):
        #         return val - 1
        #     if val == len(nums) - 1:
        #         return val+1

        #Cach 3:
        n = len(nums)
        sum_expect = n * (n+1) // 2
        sum_actual = sum(nums)
        return sum_expect - sum_actual



if __name__ == "__main__":
    solution = Solution()
    nums = [0,3,1]
    res = solution.missingNumber(nums)
    print("Res: ", res)

    nums.sort()
    for i, val in enumerate(nums):
        print("i: ", i, "--", "val: ", val)
