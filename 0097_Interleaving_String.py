'''
Problem: https://leetcode.com/problems/interleaving-string/description/

My solution with Explanation and Example: https://leetcode.com/problems/interleaving-string/solutions/2832703/python-explanation-example-backtracking-w-cacheing-faster-than-93-43-ms/

Execution time: 43 ms (faster than 93.39%)
Memory usage: 16.8 MB (smaller than 5.56%)
Time complexity: O(n)
Space complexity: O(n)

'''

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3): return False

        cache = {("", "", ""): True}

        def helper(s1: str, s2: str, s3: str) -> bool:
            if (s1, s2, s3) in cache: return cache[(s1, s2, s3)]
        
            if s1 and s1[0] == s3[0]:
                if helper(s1[1:], s2, s3[1:]):
                    return True
            if s2 and s2[0] == s3[0]:
                if helper(s1, s2[1:], s3[1:]):
                    return True

            cache[(s1, s2, s3)] = False
            return False

        return helper(s1, s2, s3)
