from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
# Cach 1
        length = len(nums)
        prefix = [1]*length
        postfix = [1]*length
        res = [0]*length

        for i in range(1, length):
            prefix[i] = prefix[i-1] * nums[i-1]
        print(prefix)

        for i in range(length - 2, -1, -1):
            postfix[i] = postfix[i+1] * nums[i+1]
        for i in range(length):
            res[i] = prefix[i] * postfix[i]
        print(postfix)
        return res

if __name__ == "__main__":
    solution = Solution()
    nums = [1, 2, 3, 4]
    res = solution.productExceptSelf(nums)
    print(res)