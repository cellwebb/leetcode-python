'''
Link to problem: https://leetcode.com/problems/largest-rectangle-in-histogram/

# Problem Description
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

# Approach
1. Create a stack to keep track of locations of "left corners"
2. Move iteratively from left to right, with each new number check if it's larger or smaller
    1. if larger, append the current index to the stack
    2. if smaller, pop left corners from the stack and calculate the area, updating the max if needed
        1. Once the stack only has ids with heights smaller than the current id, stop popping and replace the height of the last popped index with the current height
        2. Instead of appending the current index to the stack, append the last popped index
        3. These actions set us up for calculating the area of a "flattened" future rectangle ("underneath the spikes")
3. Once we reach the end, we go through the stack from beginning to end, calculating the area with the right edge as the right boundary

My solution on leetcode: https://leetcode.com/problems/largest-rectangle-in-histogram/solutions/2791083/python3-stacks-solution-beats-9884/

Execution time: 955 ms (faster than 98.88%)
Memory usage: 45.8 MB (best was 22.1 MB)
Time complexity: O(n)
Space complexity: O(n)
'''

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        calc_area = lambda l, r, h: (r - l + 1) * h

        n = len(heights)
        if n == 1:
            return heights[0]
            
        max_area = 0
        stack = [0]
        for i in range(1, n):
            h = heights[i]
            if h > heights[stack[-1]]:
                stack.append(i)
                
            elif h < heights[stack[-1]]:
                while stack and h < heights[stack[-1]]:
                    j = stack.pop(-1)
                    max_area = max(max_area, calc_area(j, i-1, heights[j]))

                heights[j] = heights[i]
                stack.append(j)

        max_area = max(max_area, max((calc_area(i, n-1, heights[i]) for i in stack)))

        return max_area
