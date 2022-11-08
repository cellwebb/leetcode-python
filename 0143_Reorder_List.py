'''
Link to problem: https://leetcode.com/problems/reorder-list/

### Problem Description
You are given the head of a singly linked-list. The list can be represented as:
L0 → L1 → … → Ln - 1 → Ln
Reorder the list to be on the following form:
L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …
You may not modify the values in the list's nodes. Only nodes themselves may be changed.
### End Description


# Approach
- We will use a double-ended queue (`deque`) to maintain the original order of the nodes
- We will alternate popping from the right and left sides of the queue to get the desired reorder
- Once we deplete the queue, we will set the last nodes `.next` attribute to `None` so there isn't a cycle in the list

My solution on leetcode: https://leetcode.com/problems/reorder-list/solutions/2794563/python3-simple-explanation-faster-than-95-55-double-ended-queue-90-ms/

Execution time: 90 ms (faster than 95.55%)
Memory usage: 24.2 MB (smaller than 27.62%; best is 22 MB)
Time complexity: O(n)
Space complexity: O(n)

'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from collections import deque

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        """Do not return anything, modify head in-place instead."""
        
        node = head
        q = deque()  # we will not add the head to the queue
        while node.next:
            node = node.next
            q.append(node)
        
        node = head
        while q:
            node.next = q.pop()
            node = node.next
            if q:
                node.next = q.popleft()
                node = node.next
        
        node.next = None

```

Please upvote if you found this helpful! :)
