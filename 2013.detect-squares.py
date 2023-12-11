# Approach: Geometry + Hashmap
class DetectSquares:
    # Complexity: O(1)
    def __init__(self):
        # Maintain count of each point using hashmap to keep track of same point
        # added multiple times. "int defaultdict" avoids KeyError by returning 0
        # for non-existing keys.
        self.counts = collections.defaultdict(int)

    # Complexity: O(1)
    def add(self, point: List[int]) -> None:
        # Add a point by incrementing its count in the hashmap.
        self.counts[tuple(point)] += 1

    # Complexity: O(n)
    def count(self, point: List[int]) -> int:
        x0, y0 = point
        squares = 0

        # Iterate over all points seen so far.
        for (x, y) in list(self.counts.keys()):
            # A point can make a diagonal with query point only if their their x
            # (square's length) and y (square's breadth) coordinates are offset
            # by equal distances. Also, both points must not be same to avoid
            # counting squares with 0 area.
            if abs(x0-x) == abs(y0-y) and (x, y) != (x0, y0):

                # Using one diagonal's ends, the second diagonal's expected ends
                # can be found and queried in the hashmap. If some point has
                # multiple occurence, all its occurences can make a separate
                # square with the other three points. Thus, occurences of all
                # points are multiplied together. If a point, has no occurences
                # it multiplies a 0 in the expression as no square is possible.
                squares += (self.counts[(x, y)]
                            * self.counts[(x0, y)]
                            * self.counts[(x, y0)])

        # Return total count of possible squares.
        return squares


# Your DetectSquares object will be instantiated and called as such:
# obj = DetectSquares()
# obj.add(point)
# param_2 = obj.count(point)
