from typing import List
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        k = 0

        for i in range(len(nums)):
            if nums[i] != val:
                nums[k] = nums[i]
                k += 1
        return k

if __name__ == "__main__":
    solution1 = Solution()
    num1 = [3,2,2,3]
    value = 3

    print("Before: ", num1)

    k = solution1.removeElement(num1, value)
    print("After: ", num1[:k])