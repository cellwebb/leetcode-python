'''
# Approach
1. Start with a pointer on each end
    1. `l = 0`
    2. `r = len(height) - 1`
2. Calculate the area (base x height) which can hold water
    1. base = distance between `l` and `r`
    2. height = the lesser of `l` and `r`'s values in `height`
3. Update `max_area` if the calculated area is greater
4. Using their indexed values in `height`, move `l` and `r` together based on which is shorter
5. Repeat steps 2 to 4 until `l` and `r` meet somewhere in the middle
6. Return the `max_area`

https://leetcode.com/problems/container-with-most-water/description/
'''

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_area = 0
        
        l = 0
        r = len(height) - 1
        
        while l < r:
            base = r - l
            h = min(height[l], height[r])

            if base * h > max_area:
                max_area = base * h

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_area
