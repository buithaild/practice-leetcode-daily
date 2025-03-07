# Given an array nums of n integers where nums[i] is in the range [1, n], return an array of
# all the integers in the range [1, n] that do not appear in nums.
from typing import List


class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        ret = []
        set_nums = set(nums)
        for i in range(1, len(nums) + 1):
            if i not in set_nums:
                ret.append(i)
        return ret


if __name__ == "__main__":
    s = Solution()
    nums = [4,3,2,7,8,1,2,3]

    res = s.findDisappearedNumbers((nums))
    print(res)

    print("Set: ", set(nums)) #Khong chua phan tu trung lap