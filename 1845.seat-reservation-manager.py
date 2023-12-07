# Approach: Minheap
class SeatManager:
    # Complexity: O(n)
    def __init__(self, n: int):
        # Initialize "avail" heap with all seats as none are reserved right now.
        self.avail = [seat for seat in range(1, n+1)]

    # Complexity: O(logn)
    def reserve(self) -> int:
        # Minheap's root = Minimum unreserved seat.
        return heapq.heappop(self.avail)

    # Complexity: O(logn)
    def unreserve(self, seatNumber: int) -> None:
        # Push any unreserved seats back to "avail" heap.
        heapq.heappush(self.avail, seatNumber)

# Your SeatManager object will be instantiated and called as such:
# obj = SeatManager(n)
# param_1 = obj.reserve()
# obj.unreserve(seatNumber)
