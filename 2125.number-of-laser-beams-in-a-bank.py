class Solution:
    # Approach: Greedy + Math (Combinations), Complexity: O(m*n), O(1)
    def numberOfBeams(self, bank: List[str]) -> int:
        # Return number of devices given a row as binary string.
        def countDevs(row: str) -> int:
            dev_count = 0
            for ch in row:
                if ch == '1':
                    dev_count += 1
            return dev_count

        prev = devices = beams = 0

        # Iterate over each row of floor.
        for row in bank:
            # Count the number devices on current row.
            devices = countDevs(row)
            # Skip rows without any devices.
            if not devices:
                continue

            # Every device in the previous row sends a beam to every device in
            # current row. Sum the beams across the entire floor into "beams".
            # Number of beams = (devices in prev row) X (devices in current row).
            beams += devices * prev

            # Devices in current row are previous for next row.
            prev = devices

        # Return total number of beams across the floor.
        return beams
