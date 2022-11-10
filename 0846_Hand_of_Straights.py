'''
Link to problem: https://leetcode.com/problems/hand-of-straights/

### Problem Description
Alice has some number of cards and she wants to rearrange the cards into groups so that each group is of size `groupSize`, and consists of `groupSize` consecutive cards.

Given an integer array hand where `hand[i]` is the value written on the `ith` card and an integer `groupSize`, return `true` if she can rearrange the cards, or `false` otherwise.
### End Description

# Intuition
Reasons why the hand would be incapable:
1. There would be any groups with leftover cards
2. At any point, there are not enough unique cards remaining
3. The hand does not increment 1-by-1
4. Not having enough of a needed card

For any card in the hand with group_size=N, there are N possible variations of valid consecutive groups. For example, with `group_size = 3` there are 3 variations:
- `x,   x+1, x+2`
- `x-1, x,   x+1`
- `x-2, x-1, x`

For either the lowest or highest end of numbers there is only one variation: `x, x+1, x+2` for numbers on the low end, and `x-2, x-1, x` on the high end. Using this we can start from either end and iteratively remove valid groups (removing duplicate groups all at once).

Operating this way, we either end up with all cards distributed into valid groups, or we won't have enough of a needed card (Reason #4). For our approach, we will start with cards on the low end and increment upwards.

# Approach

1. We first eliminate hands with lengths which are not multiples of `group_size` (Reason #1)
2. Create a `Counter()` for `hand`
3. Create a sorted set of the unique cards
4. While loop:
    1. If there are fewer than `group_size` cards in `unique_cards`, the hand is invalid (Reason #2)
    2. Pull the lowest n unique cards from `unique_cards` and assign it to `group`
    3. If the cards are consecutive, the lowest and highest among them will have a difference of `group_size - 1`. If the difference is anything but, the hand is invalid (Reason #3)
    4. Check the lowest card's count for the minimum needed (`min_count`) and remove it from `c` and `unique_keys`
    5. Iterate through the remaining cards in the group. If there are not enough cards, the hand is invalid (Reason #4). If `c` contains exactly enough cards, delete the card from `c` and remove the card crom `unique_cards`. Otherwise, subtract the needed cards from `c`.
5. If all cards are distributed into valid groups, the while loop exits and we `return True`


Execution time: 237 ms (faster than 84.75%)
Memory usage: 16.4 MB
Time complexity: O(n)
Space complexity: O(n)

My solution on leetcode: https://leetcode.com/problems/hand-of-straights/solutions/2801626/python-easy-to-follow-with-explanation-237-ms-faster-than-84-75/

'''

from collections import Counter

class Solution:
    def isNStraightHand(self, hand: List[int], group_size: int) -> bool:
        if len(hand) % group_size != 0: return False
        c = Counter(hand)
        unique_cards = sorted(set(c.keys()))
        while c:
            if len(unique_cards) < group_size: return False

            group = unique_cards[:group_size]
            if group[-1] - group[0] != group_size - 1: return False

            min_count = c[group[0]]
            del c[group[0]]
            unique_cards.remove(group[0])

            for card in group[1:]:
                if c[card] > min_count:
                    c.subtract({card: min_count})
                elif c[card] == min_count:
                    del c[card]
                    unique_cards.remove(card)
                else:
                    return False

        return True
