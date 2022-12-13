'''
Problem: https://leetcode.com/problems/valid-palindrome-ii/
My Explanation: https://leetcode.com/problems/valid-palindrome-ii/solutions/2906727/

Runtime: 70 ms (Beats 99.69%)
Memory: 14.5 MB (Beats 89.91%)
'''

class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True

        l = 0
        r = len(s) - 1

        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                tmp1 = s[:l] + s[l+1:]
                tmp2 = s[:r] + s[r+1:]
                if tmp1 == tmp1[::-1] or tmp2 == tmp2[::-1]:
                    return True
                else:
                    return False

        return True
