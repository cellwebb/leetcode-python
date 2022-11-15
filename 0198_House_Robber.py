'''
Link to problem: https://leetcode.com/problems/house-robber/

### Problem Description
You are a professional robber planning to rob houses along a street. Each house has a certain amount
of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses
have security systems connected and it will automatically contact the police if two adjacent houses
were broken into on the same night.

Given an integer array `nums` representing the amount of money of each house, return the maximum amount
of money you can rob tonight without alerting the police.
### End Description

# Intuition
- At every house we will have two options: rob or skip
- Because we cannot rob a house that is next door to another, and because all values will be non-negative,
  we will always leave either one or two houses unrobbed between robbed houses.
- Given the conditions, it will never make sense to skip three or more houses in a row since we could
  rob houses in-between.

# Approach
1. `bag` is the amount stolen so far, starting from zero, with two options for having skipped the previous
   house or potentially robbed the previous house
   a. `bag[0]` is the amount we'll have if we have skipped the previous house
   b. `bag[1]` is the max of skipping vs robbing the previous house
   c. If we choose to skip twice in a row, `bag[0]` and `bag[1]` will be equal, so it will always be best
      to rob the following house
2. During each iteration:
   a. Pull the next value from `nums` and assign it to `house`
   b. Add `bag[0] + house` and compare it to `bag[1]`
   c. Simultaneously, move `bag[1]` to `bag[0]` and update `bag[1]` to the max of the previous step
3. At the end of the iterations, return `bag[1]` as that is the max possible haul of stolen goods
   
# Example
start:
`nums = [2, 7, 9, 3, 1]; bag = (0, 0)`

iterations:
- `house = 2; bag = (0, 0)` -> `bag = (0, 2)`
  - `bag[1]` moves to `bag[0]`
  - `bag[1]` becomes 2 because 0 + 2 > 0
- `house = 7; bag = (0, 2)` -> `bag = (2, 7)`
  - `bag[1]` moves to `bag[0]`
  - `bag[1]` becomes 7 because 0 + 7 > 2
- `house = 9; bag = (2, 7)` -> `bag = (7, 11)`
  - `bag[1]` moves to `bag[0]`
  - `bag[1]` becomes 11 because 2 + 9 > 7
- `house = 3; bag = (7, 11)` -> `bag = (11, 11)`
   - `bag[1]` moves to `bag[0]`
   - `bag[1]` stays at 11 because 7 + 3 < 11
- `house = 1; bag = (11, 11)` -> `bag = (11, 12)`
   - `bag[1]` moves to `bag[0]`
   - `bag[1]` becomes 12 because 11 + 1 > 11

end:
Return bag[1] -> 12

It could be looked at as if, with each iteration, we are appending the new value and chopping off every
element but the last two.


Execution time: 30 ms (faster than 96.97%)
Memory usage: 13.9 MB (smaller than 19.80%)
Time complexity: O(n)
Space complexity: O(n)

My solution on leetcode: https://leetcode.com/problems/house-robber/solutions/2818729/python3-four-lines-w-explanation-faster-than-96-97-dynamic-programming/
'''

class Solution:
    def rob(self, nums: List[int]) -> int:
        bag = (0, 0)

        for house in nums:
            bag = (bag[1], max(bag[0] + house, bag[1]))  # (amount if we skip this house, 

        return bag[1]
