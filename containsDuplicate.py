from typing import List
class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        ## C1
        # nums.sort()
        #
        # for i in range(1, len(nums)):
        #     if nums[i] == nums[i-1]:
        #         return True
        # return False


        ## Cach 2
        # mySet = set()
        # for n in nums:
        #     if n in mySet:
        #         return True
        #     mySet.add(n)
        # return  False



if __name__ == "__main__":
    solution = Solution()
    nums = [1,2,3,1]
    res = solution.containsDuplicate(nums)
    print(res)