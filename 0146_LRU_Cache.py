'''
Link to problem: https://leetcode.com/problems/lru-cache/

### Problem Description
Design a data structure that follows the constraints of a Least Recently Used (LRU) cache.

Implement the LRUCache class:
* `LRUCache(int capacity)` Initialize the LRU cache with **positive** size capacity.
* `int get(int key)` Return the value of the `key` if the key exists, otherwise return `-1`.
* void put(int key, int value) Update the value of the `key` if the key exists. Otherwise, add the key-value pair to the cache.
    * If the number of keys exceeds the `capacity` from this operation, evict the least recently used key.

The functions get and put must each run in `O(1)` average time complexity.
### End Description


# Approach
- When we initialize, we create two attributes, an int for tracking capacity, and an OrderedDict (OD)
- In addition to holding key-value pairs, ODs track the order pairs are added, so you can OD.popitem() to remove the most recent, or OD.popitem(last=False) to remove the least recent
    - For this problem we only want to use OD.popitem(last=False)
- OD.put()
    - As we add new keys to the OD, we decrement capacity
    - Once the capacity is reached, when new keys are added we use OD.popitem(last=False) to remove the least recently used key
    - If OD.put() is used to assign a new value to a key, we move it to the most recently used key by first deleting the old entry from OD
- OD.get()
    - if key is in OD, we move it to most recent by deleting the entry and re-adding it before returning the value
    - If key isn't in OD, we return -1
    
My solution: https://leetcode.com/problems/lru-cache/solutions/2794213/python-ordereddict-solution-explained-faster-than-96-10/

Execution time: 780 ms (faster than 96.10%)
Memory usage: 78.7 MB (smaller than 90.22%)
Time complexity: O(n) where n is the number of `get` and `put` actions (each get & put action runs in O(1) time complexity)
Space complexity: O(n) where n is capacity
'''

# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)

from collections import OrderedDict

class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.d = OrderedDict()

    def get(self, key: int) -> int:
        if key in self.d:
            value = self.d[key]

            # move key-value to most recent
            del self.d[key]
            self.d[key] = value

            return value
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key not in self.d:
            if self.capacity > 0:
                self.capacity -= 1
            else:
                # remove least recently used key-value pair
                self.d.popitem(last=False)
        else:
            # move key to most recent (with new value)
            del self.d[key]

        self.d[key] = value

```

Please upvote if this was helpful
