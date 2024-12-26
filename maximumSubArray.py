from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:

#Cach 1
        # res = nums[0]
        # total = 0
        #
        # for n in nums:
        #     if total < 0:
        #         total = 0
        #     total += n
        #     res = max(res, total)
        # return res

#Cach 2: Kadane
        res = nums[0]
        maxEnd = nums[0]

        for i in range(1, len(nums)):

            maxEnd = max(maxEnd + nums[i], nums[i])
            res = max(res, maxEnd)
        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, -7, 3, 4]
    res = solution.maxSubArray(nums)
    print(res)