'''
https://leetcode.com/problems/move-zeroes/

Runtime: 175 (Faster than 89.85%)
'''

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        j = 0

        for i in range(len(nums)):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        nums[j:] = [0] * (i + 1 - j)
