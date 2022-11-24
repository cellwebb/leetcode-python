'''
Problem: https://leetcode.com/problems/edit-distance/submissions/848964576/

Runtime: 103 ms (Better than 97.59%)
Memory: 16.8 MB (Better than 80.79%)
'''

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        n, m = len(word1), len(word2)
        cache = {}

        def distance(i: int, j: int):
            if (i, j) in cache: return cache[(i, j)]
            elif i == n and j == m: return 0
            elif i == n: return m - j
            elif j == m: return n - i

            elif word1[i] == word2[j]:
                ops = distance(i+1, j+1)
            else:
                insert = 1 + distance(i, j+1)
                delete = 1 + distance(i+1, j)
                replace = 1 + distance(i+1, j+1)
                ops = min(insert, delete, replace)

            cache[(i, j)] = ops
            return ops


        return distance(0, 0)
