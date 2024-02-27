# Approach: Hashmap + Pair, Complexity: O(1) for all queries.
class UndergroundSystem:
    def __init__(self) -> None:
        # Map pair of stations -> average.
        self.avg = {}
        # Map pair of stations -> total number of trips inbetween.
        self.trips = {}
        # Map id of traveller -> (currently checked in station, check in time).
        self.checked = {}

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        # Create entry for traveller in "checked" table.
        self.checked[id] = (stationName, t)

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        # Get station checked in and time of check in via "checked" hashmap.
        src, t0 = self.checked.pop(id)
        # Destination is the check out station.
        dest = stationName
        # Duration of trip = Check out time - Check in time.
        duration = t - t0

        # If no trip has previously been made from "src" to "dest".
        if (src, dest) not in self.avg:
            # Initially Average = Trip Duration as only 1 trip took place.
            self.avg[(src, dest)] = duration
            # Initialize count of trip from src to dest = 1.
            self.trips[(src, dest)] = 1
        else:
            # Get previous average and count of trips made from src to dest.
            prev_avg, prev_trips = self.avg[(src, dest)], self.trips[(src, dest)]
            # Use them to compute new average along with duration of latest trip.
            new_avg = (prev_avg * prev_trips + duration) / (prev_trips + 1)

            # Update average in hashmap.
            self.avg[(src, dest)] = new_avg
            # Increment trip count.
            self.trips[(src, dest)] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        # Average can be returned easily as its tracked in average hashmap.
        return self.avg[(startStation, endStation)]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)
