class Solution:
    # Approach: Binary Search, Complexity: O(d*n), O(1)
    # where, d -> range of values in "bloomDay"

    def minDays(self, bloomDay: List[int], m: int, k: int) -> int:
        # Count number of bouquets that can be prepared.
        def countBouq(pick_day: int):
            bouq = streak = 0

            for day in bloomDay:
                # If a budding flower is found, all consecutively bloomed flowers
                # collected till now have to be dropped.
                if day > pick_day:
                    streak = 0
                    continue

                # If a bloomed flowers is found, pick it.
                streak += 1
                # If flowers required for bouquet are picked, create bouquet.
                # Now pick next batch of k flowers for next bouquet.
                if streak == k:
                    bouq += 1
                    streak = 0

            # Return number of bouquets made.
            return bouq

        # Picking on bday of first flower guarantees at least one flower can be
        # picked. Picking on bday of last flower lets all flowers to be picked.
        beg, end = min(bloomDay), max(bloomDay)

        # Binary search to minimize picking day which picks at least m bouquets.
        while beg < end:
            mid = beg + (end - beg) // 2
            if countBouq(mid) >= m:
                end = mid
            else:
                beg = mid + 1

        # Validation for edge cases with no solution.
        if countBouq(beg) >= m:
            return beg
        return -1
