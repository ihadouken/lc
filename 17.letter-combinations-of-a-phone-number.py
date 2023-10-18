class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        # If there are no digits, there are no combinations.
        if not digits:
            return []

        # Define letters corresponding with each digit.
        letters = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        # Use extra array to store current combination.
        comb = []
        res = []

        def generate(index: int) -> None:
            # If one letter for each digit has been selected, a valid combination
            # is formed.
            if len(comb) == len(digits):
                res.append(''.join(comb))
                return

            # Iterate over all letters for current digit's position.
            for ch in letters[digits[index]]:
                comb.append(ch)

                # Recursively select a char for the next digit's position after
                # selecting one of the chars for the current digit's index.
                generate(index+1)

                # Backtrack and try other chars mapping to the digit.
                comb.pop()

        # Initially try to select a char at the first position.
        generate(0)
        # Return the list of all combinations.
        return res
