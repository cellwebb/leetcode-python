'''
Problem URL: https://leetcode.com/problems/detect-squares/

### Problem Description
You are given a stream of points on the X-Y plane. Design an algorithm that:
 - Adds new points from the stream into a data structure. Duplicate points are allowed
   and should be treated as different points.
 - Given a query point, counts the number of ways to choose three points from the data
   structure such that the three points and the query point form an axis-aligned square
   with positive area.

An **axis-aligned square** is a square whose edges are all the same length and are either
parallel or perpendicular to the x-axis and y-axis.

Implement the `DetectSquares` class:
 - `DetectSquares()` Initializes the object with an empty data structure.
 - `void add(int[] point)` Adds a new point `point = [x, y]` to the data structure.
 - `int count(int[] point)` Counts the number of ways to form axis-aligned squares with
   point `point = [x, y]` as described above.
### End Description


# Approach

## Adding Points
Since duplicate points can be used to form multiple distinct, countable squares, we will
convert the point from a list to a tuple so we can track the number of times it has been
added in a dictionary.

*Note: `defaultdict(int)` defaults to 0 for new values*


## Counting Squares
To reduce the amount of iterating, we loop through the items of `self.points` searching
for points that can serve as the opposite corner of a square. For each such point found,
we check if `self.points` contains the other two necessary corners. If so, we calculate
how many identical squares can be created by multiplying the instances of each of the
three points in `self.points`. We add this number to the running count, which we return
once the for loop is completed.


Execution time: 378 ms (faster than 90.28%)
Memory usage: 15.9 MB (smaller than 63.45%)
Time complexity: O(n)
Space complexity: O(n)

My solution on leetcode: https://leetcode.com/problems/detect-squares/solutions/2764859/python3-simple-fast-elegant-beats-90/

'''

from collections import defaultdict

class DetectSquares:

    def __init__(self):
        self.points = defaultdict(int)

    def add(self, point: List[int]) -> None:
        self.points[tuple(point)] += 1

    def count(self, point: List[int]) -> int:
        square_count = 0
        x1, y1 = point

        for (x2, y2), n in self.points.items():
            x_dist, y_dist = abs(x1 - x2), abs(y1 - y2)
            if x_dist == y_dist and x_dist > 0:
                corner1 = (x1, y2)
                corner2 = (x2, y1)
                if corner1 in self.points and corner2 in self.points:
                    square_count += n * self.points[corner1] * self.points[corner2]

        return square_count
