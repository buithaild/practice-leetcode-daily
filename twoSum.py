from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        prev = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in prev:
                return [prev[diff], i]
            prev[num] = i

if __name__ == "__main__":
    solution = Solution()
    myList = [2,1,5,3]
    target = 4
    res = solution.twoSum(myList, target)
    print(res)