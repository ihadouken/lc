class Solution:
    # Approach: Graph + BFS, Complexity: O(n), O(sqrt(n))
    # Note: In the worst case, the matrix is square with M = N = sqrt(n). Max.
    #       elements in queue = size of largest diagonal = sqrt(n).
    # Tip: For any square, there is a square belonging to next diagonal to its
    #      right except square in the first column which has an extra neighbour
    #      to its bottom. First diagonal always has one element i.e. (0, 0).
    #      Initiate a BFS on the first diagonal. The BFS queue traverses the
    #      grid/graph level (diagonal) wise.

    def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
        res = []
        q = collections.deque()
        q.append((0, 0))

        while q:
            x, y = q.popleft()

            # Ensure that the search remains in bounds.
            if x >= len(nums) or y >= len(nums[x]):
                continue

            # Process the cell before moving on to its neighbours.
            res.append(nums[x][y])

            # Add bottom neighbour of element in first column.
            if y == 0:
                q.append((x+1, y))

            # Add right neighbour of every element to get next level (diagonal).
            q.append((x, y+1))

        # Diagonal traversal = BFS traversal
        return res


    # Approach: Hashmap, Complexity: O(n), O(n) where n -> number of elements
    # Tip: Elements in the same diagonal have equal sum of indices.

    # def findDiagonalOrder(self, nums: List[List[int]]) -> List[int]:
    #     diagonals = collections.defaultdict(list)
    #     res = []
    #
    #     # Organize elements into diagonal lists via the sum of their indices.
    #     for i, row in enumerate(nums):
    #         for j, element in enumerate(row):
    #             diagonals[i+j].append(element)
    #
    #     # Create the result list by combining the diagonal lists. Concatenation
    #     # in reverse order as elements are required to be visited bottom to top.
    #     for d in diagonals.values():
    #         res.extend(reversed(d))
    #     return res
