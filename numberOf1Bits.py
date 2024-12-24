# Binary
class Solution:
    def hamingWeight(self, n: int) -> int:
        res = 0
        for i in range(32):
            if (n >> i) & 1:
                res += 1
        return res

if __name__ == "__main__":
    solution = Solution()
    n = 11 #(11: 1011)
    res = solution.hamingWeight(n)
    print(res)