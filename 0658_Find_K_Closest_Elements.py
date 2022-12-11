'''
Problem: https://leetcode.com/problems/find-k-closest-elements/

Runtime: 324 ms (Better than 87.58%)
Memory: 15.5 MB (Better than 80.72%)
'''

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        if k == len(arr): return arr
        if x <= arr[0]: return arr[:k]
        if x >= arr[-1]: return arr[-k:]

        if k == 1 and x not in arr:
            i = bisect.bisect_left(arr, x)
            return [arr[i-1] if x - arr[i-1] <= arr[i] - x else arr[i]]

        l = r = bisect.bisect(arr, x) - 1
        while r - l + 1 < k:
            if l == 0:
                r = k - 1
            elif r == len(arr) - 1:
                l = len(arr) - k
            elif x - arr[l-1] <= arr[r+1] - x:
                l -= 1
            else:
                r += 1

        return arr[l:r+1]
