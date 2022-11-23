'''
Problem: https://leetcode.com/problems/subsets-ii/description/
Explanation of my solution: https://tinyurl.com/3vfhhruu

Runtime: 35 ms (Beats 97.15%)
Memory: 14.1 MB (Beats 93.26%)
'''

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        subsets_by_index = [[]] + [x for i in range(1, len(nums) + 1) for x in combinations(range(len(nums)), i)]
        
        subsets = set()
        for sub_by_id in subsets_by_index:
            subsets.add(tuple(sorted(nums[i] for i in sub_by_id)))

        return subsets
