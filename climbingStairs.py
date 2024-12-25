from typing import List

class Solution:
    def climbingStair(self, step: int) -> int:
        if step <= 3:
            return step
        prev1 = 3
        prev2 = 2
        cur = 0
        for i in range(3, step):
            cur = prev1 + prev2
            prev2 = prev1
            prev1 = cur
        return cur
if __name__ == "__main__":
    solution = Solution()
    step = 5
    res = solution.climbingStair(step)
    print(res)