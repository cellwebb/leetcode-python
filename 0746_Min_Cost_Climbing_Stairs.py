'''
Problem: https://leetcode.com/problems/min-cost-climbing-stairs/

Runtime: 76 ms (Better than 79.70%)
Memory: 14 MB (Better than 75.68%
'''

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [0] * (len(cost) + 2)

        for i, c in enumerate(cost, start = 2):
            dp[i] = c + min(dp[i-1], dp[i-2])

        return min(dp[-2:])
