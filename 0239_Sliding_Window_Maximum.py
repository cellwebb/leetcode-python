'''
# Approach

- This approach uses a combination of two pointers and a heap (aka priority) queue
- Both pointers begin at zero. `l` only begins incrementing after the window size has been reached
- During each iteration, `r` encounters a new value in `nums`, which is added to the heap along with its index (`r`) and a sort value (`-nums[r]`)
    - Heaps are automatically sorted smallest to largest, so in order to be able to retrieve/toss the largest values, an inverted sort value must be included
    - Heaps sort tuples by each tuple's first element, with ties resorting to the second element, and so on. We want to pull out the earliest instances of numbers, so the ideal order of the tuples added to the heap is: (**sort value, index, true value**)
- If we've reached the window size, we look at the top tuple of the heap, throwing them away if necessary until the top tuple has an index between `l` and `r` (inclusive)
- We then append the non-inverted, true value of the top tuple (`h[0][2]`) to `res`
- After the completion of the while loop, we return `res`

https://leetcode.com/problems/sliding-window-maximum/description/
'''

from heapq import heappush, heappop

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        res = []
        h = []
        
        window_size = lambda l, r: r - l + 1
        
        l = 0
        r = -1  # set to -1 so it immediately moves to 0

        while r < len(nums) - 1:
            r += 1
            if window_size(l, r) > k: l += 1
            
            heappush(h, (-nums[r], r, nums[r])) # sort value, index, true value
            
            while not (l <= h[0][1] <= r):
                heappop(h)
                
            if window_size(l, r) == k:
                max_val = h[0][2]
                res.append(max_val)

        return res
