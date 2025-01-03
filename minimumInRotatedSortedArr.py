from typing import List
class Solution:
    def minimumRotatedSortedArr(self, nums: List[int]) -> int:
        # #Cach 1:
        # res = nums[0]
        # for i in range(1, len(nums)):
        #     res = min(res, nums[i])
        # return res

        #Cach 2
        low = 0
        high = len(nums) - 1

        while low < high:
            if (nums[low] < nums[high]):
                return nums[low]
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1
            else:
                high = mid
        return nums[low]

if __name__ == "__main__":
    solution1 = Solution()
    num1 = [3,4,5,-1,2,3]
    result = solution1.minimumRotatedSortedArr(num1)
    print(result)