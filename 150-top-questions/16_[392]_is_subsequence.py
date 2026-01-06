"""
Given two strings s and t, return true if s is a subsequence of t, or false otherwise.

A subsequence of a string is a new string that is formed from the original string by deleting some (can be none) of the characters without disturbing the relative positions of the remaining characters. (i.e., "ace" is a subsequence of "abcde" while "aec" is not).



Example 1:

Input: s = "abc", t = "ahbgdc"
Output: true
Example 2:

Input: s = "axc", t = "ahbgdc"
Output: false

"""

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        s_point = 0
        t_point = 0

        while s_point < len(s) and t_point < len(t):
            if s[s_point] == t[t_point]:
                s_point += 1
            t_point += 1

        return s_point == len(s)

if __name__ == '__main__':
    s = Solution()
    str1 = "abc"
    str2 = "ahbgdc"
    res = s.isSubsequence(str1, str2)
    print(res)

    str3 = "axc"
    str4 = "ahbgdc"
    res2 = s.isSubsequence(str3, str4)
    print(res2)