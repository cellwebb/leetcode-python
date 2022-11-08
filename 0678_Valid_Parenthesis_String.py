'''
678. Valid Parenthesis String

- Create two double-ended queues, one for keeping track of `(` indices and the other for keeping track of `*` indices
- Iterate over the string, right-appending the indices of `(` and `*` to their respective queues
- When a `)` is encountered, right-pop the last appended `(`
    - If no `(` are available to be popped, try left-popping the earliest `*`
    - If no `*` are available to be popped, we can conclude the string is invalid and return `False`
- Once s has been fully traversed, left-pop the `(` queue and hold onto the index
    - Left-pop from the `*` queue until we get a greater index
    - If no `*` are available to be popped, we can conclude the string is invalid and return `False`
- Continue the process of left-popping from both queues until the end of either is reached
    - If we run out of `*` before `(`, we can conclude the string is invalid and return `False`
    - Otherwise, we can return `True`!

https://leetcode.com/problems/valid-parenthesis-string/description/
'''

from collections import deque

class Solution:
    def checkValidString(self, s: str) -> bool:
        left_parentheses = deque()
        wildcards = deque()

        for i, char in enumerate(s):
            if char == '(':
                left_parentheses.append(i)
            elif char == ')':
                if left_parentheses:
                    left_parentheses.pop()
                elif wildcards:
                    wildcards.popleft()
                else:
                    return False
            else:
                wildcards.append(i)

        while left_parentheses:
            i = left_parentheses.popleft()

            while wildcards and wildcards[0] < i:
                wildcards.popleft()

            if wildcards:
                wildcards.popleft()
            else:
                return False

        return True
