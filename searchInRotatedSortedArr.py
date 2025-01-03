from typing import List
class Solution:
    def minimumRotatedSortedArr(self, nums: List[int], key: int) -> int:
        low = 0
        high = len(nums) - 1

        while low <= high:
            mid = (high + low) // 2

            if nums[mid] == key:
                return mid

            if nums[mid] >= nums[low]: #Truong hop ben trai duoc sap xep tang dan
                if key >= nums[0] and key < nums[mid]:
                    high = mid - 1
                else:
                    low = mid + 1

            else: #TRuong hop ben phai duoc sap xep tang dan
                if key > nums[mid] and key <= nums[high]:
                    low = mid + 1
                else:
                    high = mid - 1
        return -1
if __name__ == "__main__":
    solution = Solution()
    num = [5, 6, 7, 8, 9, 10, 1, 2, 3]
    result = solution.minimumRotatedSortedArr(num, 3)
    print(result)
