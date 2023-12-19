# Approach: Maxheap + Hashmap + Lazy Modification
class FoodRatings:
    # Complexity: O(n)
    def __init__(self, foods: List[str], cuisines: List[str], ratings: List[int]):
        # Store correct rating for every food.
        self.ratings = {}
        # Hashmap to lookup cuisine for food in changeRating().
        self.food2cuisine = {}
        # Every cuisine's foods are stored in separate maxheap.
        self.cus_heaps = collections.defaultdict(list)

        for f, c, r in zip(foods, cuisines, ratings):
            # Add food to cuisine's maxheap. Use -ve rating to emulate maxheap.
            # Food name automatically acts as second parameter for lexicographic
            # increasing sorting requirement.
            self.cus_heaps[c].append((-r, f))

            # Populate food -> cuisine mapping for use in changeRating().
            self.food2cuisine[f] = c

            # Initialize food rating in ratings hashmap.
            self.ratings[f] = -r

        # Heapify all cuisine maxheaps.
        for maxheap in self.cus_heaps.values():
            heapq.heapify(maxheap)

    # Complexity: (logn)
    def changeRating(self, food: str, newRating: int) -> None:
        # Find the cuisine of given food dish.
        c = self.food2cuisine[food]

        # Update rating for food in ratings hashmap.
        self.ratings[food] = -newRating

        # Insert the food again into the cuisine's heap with newer rating. All
        # higher ratings for food will be invalided by rating hashmap. All lower
        # ratings can't be reached until newly added rating holds.
        heapq.heappush(self.cus_heaps[c], (-newRating, food))

    # Complexity: (logn)
    def highestRated(self, cuisine: str) -> str:
        # Determine the heap associated with given cuisine.
        cus_heap = self.cus_heaps[cuisine]

        # Return food with first (highest) valid rating.
        while cus_heap[0][0] != self.ratings[cus_heap[0][1]]:
            heapq.heappop(cus_heap)
        return cus_heap[0][1]


# Your FoodRatings object will be instantiated and called as such:
# obj = FoodRatings(foods, cuisines, ratings)
# obj.changeRating(food,newRating)
# param_2 = obj.highestRated(cuisine)
