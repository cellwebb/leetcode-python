'''
Problem:     https://leetcode.com/problems/first-missing-positive/
Explanation: https://leetcode.com/problems/first-missing-positive/solutions/2895687/

Runtime: 263 ms (Faster than 97.59%)
'''

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        if not nums or 1 not in nums:
            return 1

        return min(set(range(1, len(nums) + 2)).difference(set(nums)))
