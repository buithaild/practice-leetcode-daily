from typing import List

class Solution:
    def threeSum(self, nums: List[int], target: int) -> List[List[int]]:
        res = []
        nums.sort()
        for i in range(len(nums) - 1):
            if(i > 0 and nums[i] == nums[i-1]):
                continue
            j = i + 1
            k = len(nums) - 1
            while j < k:
                total = nums[i] + nums[j] + nums[k]

                if total > target:
                    k -= 1
                elif total < target:
                    j += 1
                else:
                    res.append([nums[i], nums[j], nums[k]])
                    j += 1
        return res

if __name__ == "__main__":
    solution = Solution()
    myList = [-4,-1,-1,0,1,2]
    target = 0
    res = solution.threeSum(myList, target)
    print(res)
