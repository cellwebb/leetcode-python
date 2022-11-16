'''
Link to problem: https://leetcode.com/problems/merge-k-sorted-lists/

### Problem Description
You are given an array of `k` linked-lists `lists`, each linked-list is sorted in ascending order.

Merge all the linked-lists into one sorted linked-list and return it.
### End Description

# Intuition
xxxxxxxxxx

# Approach
xxxxxxxxxx

Execution time: 168 ms (faster than 77.89%)
Memory usage: 17.9 MB (smaller than 52.20%)
Time complexity: O(n)
Space complexity: O(n)

My solution on leetcode: 
'''

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        vals = defaultdict(list)
        for ls in lists:
            node = ls
            while (node):
                vals[node.val].append(node)
                node = node.next

        head = None
        for i in sorted(vals.keys()):
            for x in vals[i]:
                if not head:
                    head = x
                    node = head
                else:
                    node.next = x
                    node = node.next

        return head
