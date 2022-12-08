'''
https://leetcode.com/problems/remove-duplicates-from-sorted-list/

Runtime: 41 ms (Better than 95.80%)
Memory: 13.9 MB (Better than 72.47%)
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # Iterates through nodes in a sorted linked list, removing nodes with duplicate values
        
        if not head:
            return None

        curr = head
        while curr.next:
            if curr.val == curr.next.val:
                curr.next = curr.next.next
            else:
                curr = curr.next

        return head
