'''
https://leetcode.com/problems/is-subsequence/submissions/849853990/

Runtime: 31 ms (Better than 96.4%)
Memory: 13.9 MB (Better than 82.7%)
'''

class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        n, m = len(s), len(t)
        i = j = 0

        while i < n and j < m:
            if s[i] == t[j]:
                i += 1
                j += 1
            elif j < m:
                j += 1
            else:
                return False

        return i == n
