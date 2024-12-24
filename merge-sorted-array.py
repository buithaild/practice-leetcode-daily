from typing import List

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        mindex = m - 1
        nindex = n - 1
        right = m + n - 1

        while nindex >= 0:
            if mindex >= 0 and nums1[mindex] > nums2[nindex]:
                nums1[right] = nums1[mindex]
                mindex -= 1
            else:
                nums1[right] = nums2[nindex]
                nindex -= 1
            right -= 1

# Test case example
if __name__ == "__main__":
    solution = Solution()
    
    # Example inputs
    nums1 = [1, 2, 3, 0, 0, 0]
    m = 3
    nums2 = [2, 5, 6]
    n = 3
    
    print("Before merge:")
    print(f"nums1: {nums1}, nums2: {nums2}")
    
    solution.merge(nums1, m, nums2, n)
    
    print("After merge:")
    print(nums1)
