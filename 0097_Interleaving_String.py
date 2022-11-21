https://leetcode.com/problems/interleaving-string/description/

```
class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s1) + len(s2) != len(s3):
            return False  # incorrect number of characters

        cache = {('', '', ''): True}  # stores our true condition and caches false results

        def helper(s1: str, s2: str, s3: str) -> bool:
            if (s1, s2, s3) in cache:
                # checks if the true condition is met or
                # if the current set of strings has already
                # been found to end in failure
                return cache[(s1, s2, s3)]
        
            if s1 and s1[0] == s3[0]:
                if helper(s1[1:], s2, s3[1:]):
                    return True
            if s2 and s2[0] == s3[0]:
                if helper(s1, s2[1:], s3[1:]):
                    return True
            cache[(s1, s2, s3)] = False
            return False

        return helper(s1, s2, s3)
```
