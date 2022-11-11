'''
Link to problem: https://leetcode.com/problems/longest-increasing-subsequence/

### Problem Description
Given an integer array nums, return the length of the longest strictly increasing subsequence.
Asubsequence is an array that can be derived from another array by deleting some or no elements without changing the order
of the remaining elements.
###

# Approach

1. Create a list, `memo`, holding an arbitrarily large number `2**31`
2. Loop backwards through `nums`
    1. Start a nested loop through `memo`, also backwards, using a range so we can update `memo`
    2. Compare the two numbers until we find a situation where the number from `nums` is smaller than the number from `memo`
    3. Once we find such a situation, we either update `memo[j+1]` or, if necessary, append to `memo`
3. When we finish the outside loop, we return the length of `memo` minus one

##### Note: `memo` is not for holding the sequence, but for storing the largest number from which we can start an increasing
subsequence with size equal to its index in `memo`.

## Example:
`nums = [10, 9, 2, 5, 3, 7, 101, 18]`
`memo = [2**31]`

Iterations:
- `n = 18` is smaller than `2**31`, so `memo = [2**31, 18]`
- `n = 101` is greater than `18` and smaller than `2**31`, so it replaces 18 in memo, `memo = [2**31, 101]`
- `n = 7` is smaller than `101`, so it gets appended, `memo = [2**31, 101, 7]`
- `n = 3` is smaller than `7`, so `memo = [2**31, 101, 7, 3]`
- `n = 5` is larger than `3` and smaller than `7`, so `memo = [2**31, 101, 7, 5]`
- `n = 2` is smaller than `5` so `memo = [2**31, 101, 7, 5, 2]`
- `n = 9` is larger than `2`, `5`, and `7`, and smaller than `101`, so `memo = [2**31, 101, 9, 5, 2]`
- `n = 10` is larger than `2`, `5`, and `9`, and smaller than `101`, so `memo = [2**31, 101, 10, 5, 2]`

We can interpret `memo` like so:
- `memo[1] = 101` so we can create a subset of size 1 starting from it: `[101]`
- `memo[2] = 10` so we can create a subset of size 2 starting from it: `[10, 101]`
- `memo[3] = 5` so we can create a subset of size 3 starting from it: `[5, 7, 101]`

The last number in `memo` is `2`, with index 4, so a subset of size 4 can be created starting from it: `[2, 3, 7, 101]`. 
This is the largest subsequence possible, so we return 4.

My solution on leetcode: https://leetcode.com/problems/longest-increasing-subsequence/solutions/2804893/python-easy-to-follow-faster-than-98-71-70-ms-dynamic-programming-memoization/

Execution time: 70 ms (faster than 98.71%)
Memory usage: 14.3 MB (best was 13.6 MB)
Time complexity: O(nlogn)
Space complexity: O(n)
'''

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        memo = [2**31]

        for n in reversed(nums):
            for j in range(len(memo) - 1, -1, -1):
                if n > memo[j]:
                    continue
                elif n == memo[j]:
                    break
                elif j == len(memo) - 1:
                    memo.append(n)
                else:
                    memo[j + 1] = n
                break

        return len(memo) - 1
