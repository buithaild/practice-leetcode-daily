# Given the array nums, for each nums[i] find out
# how many numbers in the array are smaller than it.
# That is, for each nums[i] you have to count the number of valid j's such
# that j != i and nums[j] < nums[i].
#
# Return the answer in an array.
from typing import List


class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        temp = sorted(nums)
        d = {}

        for i, val in enumerate(temp):
            if val not in d:
                d[val] = i
        print("d: ", d)
        ret = []
        for i in nums:
            ret.append(d[i])
        return ret


if __name__ == "__main__":
    s = Solution()
    nums = [8,1,2,2,3]
    res = s.smallerNumbersThanCurrent(nums)
    print(res)


