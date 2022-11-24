'''
Problem: https://leetcode.com/problems/interleaving-string/description/
Explanation: https://leetcode.com/problems/interleaving-string/solutions/2832703/

Runtime: 39 ms (Beats 96.29%)
Memory: 16.9 MB
'''
    
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False
        
        cache = {("", "", ""): True}

        def helper(s1: str, s2: str, s3: str) -> bool:
            if (s1, s2, s3) in cache: return cache[(s1, s2, s3)]

            if not s1: return s2 == s3
            if not s2: return s1 == s3

            cache[(s1, s2, s3)] = (
                s1[0] == s3[0] and helper(s1[1:], s2, s3[1:]) or
                s2[0] == s3[0] and helper(s1, s2[1:], s3[1:])
            )
            return cache[(s1, s2, s3)]

        return helper(s1, s2, s3)
