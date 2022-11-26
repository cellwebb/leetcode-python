'''
https://leetcode.com/problems/pascals-triangle/

Runtime: 38 ms (Better than 82.80%)
Memory: 13.8 MB (Better than 66.87%)
'''

class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        dp = [[1] * i for i in range(1, numRows + 1)]

        for i in range(2, numRows):
            for j in range(1, i):
                dp[i][j] = sum(dp[i-1][j-1:j+1])

        return dp
