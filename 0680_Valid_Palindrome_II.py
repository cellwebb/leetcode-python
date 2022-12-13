class Solution:
    def validPalindrome(self, s: str) -> bool:
        if s == s[::-1]: return True

        removed = False
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
