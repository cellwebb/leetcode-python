'''
https://leetcode.com/problems/merge-two-sorted-lists/

Runtime: 48 ms (beats 79.21%)
Memory: 13.9 MB
'''

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from heapq import heappush, heappop

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not (list1 or list2): return None  # edge case where neither list has anything
        res_head = ListNode()
        list3 = res_head

        nums = []
        while list1:
            heappush(nums, list1.val)
            list1 = list1.next
        while list2:
            heappush(nums, list2.val)
            list2 = list2.next

        list3.val = heappop(nums)
        while nums:
            list3.next = ListNode(val=heappop(nums))
            list3 = list3.next

        return res_head
