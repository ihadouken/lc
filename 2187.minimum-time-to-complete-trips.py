class Solution:
    # Approach: Binary Search, Complexity: O(nlogn), O(1)
    def minimumTime(self, time: List[int], totalTrips: int) -> int:
        # Find total trips completed in given available time.
        def findTrips(avail_time):
            total_trips = 0

            # Consider each bus separately as they are independant of each other.
            # Total trips made by bus = Avail time / Time reqd. for 1 trip
            for trip_time in time:
                total_trips += avail_time // trip_time

            return total_trips

        # Time must at least be equal to min reqd. time among the buses in order
        # to complete at least one trip. min * totalTrips is upper bound as it is
        # the time required for all trips to completed by one bus and thus the
        # max time sufficient (but not optimal) to complete totalTrips.
        mintime = min(time)
        l, r = mintime, mintime * totalTrips

        # Binary Search to minimize available time.
        while l < r:
            m = l + (r-l) // 2
            trips = findTrips(m)

            # If trips completed < trips required to be made, allocate more time.
            if trips < totalTrips:
                l = m + 1
            # Else if trips completed >= totalTrips, current available time may
            # or mayn't be optimal so try to further minimize but keeping it in
            # the active search space (in case it is optimal).
            else:
                r = m

        # Return min. time needed to be allocated to completed totalTrips.
        return l
