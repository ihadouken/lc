# Approach: Hashmap + Array, Complexity: O(1) for all operations.
class RandomizedSet:
    def __init__(self):
        # Use array for O(1) randomized choice among its indices.
        self.val_arr = []
        # Use Hashmap to stores value -> its index in array.
        self.val2idx = {}

    def insert(self, val: int) -> bool:
        # If a value is already stored, return False.
        if val in self.val2idx:
            return False

        # Otherwise, store it at the end of array and record the index in hm.
        self.val2idx[val] = len(self.val_arr)
        self.val_arr.append(val)
        return True

    def remove(self, val: int) -> bool:
        # If key is invalid, return False.
        if val not in self.val2idx:
            return False

        # If val to be removed is the last, simply pop it from array.
        if self.val_arr[-1] == val:
            self.val_arr.pop()
        # Otherwise, find its index from hm and overwrite that index with last
        # value to avoid gaps. After that, remove the (redundant) last value.
        else:
            index = self.val2idx[val]
            last = self.val_arr.pop()
            self.val2idx[last] = index
            self.val_arr[index] = last

        # Remove the value from the hashmap too.
        self.val2idx.pop(val)
        return True

    def getRandom(self) -> int:
        # Use randint to select an index of array and return the value at index.
        rand_idx = random.randint(0, len(self.val_arr)-1)
        return self.val_arr[rand_idx]


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
