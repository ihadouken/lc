# Complexity: Time - O(m*n), Space - O(m+n)
# Tip: Simulate school multiplication algorithm and map every digit pair
#      product to a place in final product.

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        # Reversed iteratation over both numbers like in standard multplication.
        num1 = num1[::-1]
        num2 = num2[::-1]
        # The product can have maximum m+n digits.
        product = [0] * (len(num1) + len(num2))

        for i, d1 in enumerate(num1):
            for j, d2 in enumerate(num2):
                # Multiply every digit of num1 with that of num2.
                mul = int(d1) * int(d2);
                # Map product of every digit pair to a cell in the final product.
                product[i+j] += mul % 10;
                # Carry goes into the next column.
                product[i+j+1] += mul // 10;

                # If any digit place in product exceeds 9 due to product of
                # previous digits of num1, we must use a carry.
                if product[i+j] > 9:
                    product[i+j+1] += product[i+j] // 10
                    product[i+j] %= 10;

        # Remove unused columns i.e. trailing zeroes from product.
        while (len(product) > 1 and product[-1] == 0):
            product.pop()
        product.reverse()

        # Convert array to string before returning.
        return ''.join(map(str, product))
