'''
Problem: https://leetcode.com/problems/combination-sum-ii/

Runtime: 75 ms (better than 91%)
Memory: 14 MB
'''

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        combos = set()

        def helper(candidates: tuple[int], curr_val: int, curr_nums: tuple[int]) -> None:
            for i, n in enumerate(candidates):
                if i > 0 and n == candidates[i-1]: continue

                new_val = curr_val + n
                if new_val < target and candidates:
                    helper(candidates[i+1:], new_val, curr_nums + tuple([n]))
                elif new_val == target:
                    combos.add(tuple(curr_nums + tuple([n])))
                    break
                elif new_val > target:
                    break 


        candidates = tuple(sorted(x for x in candidates if x <= target))

        helper(candidates, 0, ())

        return combos
