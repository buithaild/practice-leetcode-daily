"""
HARD
There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

Each child must have at least one candy.
Children with a higher rating get more candies than their neighbors.
Return the minimum number of candies you need to have to distribute the candies to the children.



Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.
Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.
"""
from typing import List
class Solution:
    def candy(self, ratings: List[int]) -> int:
        n = len(ratings)
        total = n;
        i = 1
        while i < n:
            if ratings[i] == ratings[i-1]:
                i += 1
                continue

            current_peak = 0
            while i < n and ratings[i] > ratings[i-1]:
                current_peak += 1
                total += current_peak
                i += 1

            if i == n:
                return total

            current_valley = 0
            while i < n and ratings[i] < ratings[i-1]:
                current_valley += 1
                total += current_valley
                i += 1

            total -= min(current_peak, current_valley)
        return total

if __name__ == '__main__':
    s = Solution()
    ratings = [1,0,2]
    res = s.candy(ratings)
    print(res)
