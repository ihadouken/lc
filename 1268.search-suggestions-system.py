class Solution:
    # Approach: Sorting, Two Pointer, Complexity: O(mlogm + n)
    # where m -> number of products and n -> length of searchWord
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        products.sort()
        res = []

        l = 0
        r = len(products) - 1

        # Incrementally search products with characters from searchWord. If a
        # prefix can't match a product so can't the next prefix. Use this to
        # shortening the search space for every consecutive prefix by tightening
        # the lower and upper bounds.
        for i, ch in enumerate(searchWord):
            # If the bounds are invalid, there are no matching products.
            if l > r:
                res.append([])
                continue

            # Find the first matching word from the left.
            while l < len(products) and (i >= len(products[l]) or products[l][i] != ch):
                l += 1

            # Find the last matching word from the right.
            while r >= 0 and (i >= len(products[r]) or products[r][i] != ch):
                r -= 1

            cur = l
            matched = []

            # Try to match at most 3 products for the current prefix.
            while cur <= r and len(matched) < 3:
                matched.append(products[cur])
                cur += 1

            # Store the matches for the prefix into the result.
            res.append(matched)

        # Return the array of matches for an increasing searchWord prefix.
        return res
