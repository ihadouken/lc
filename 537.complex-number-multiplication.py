class Solution:
    # Approach: Math, Complextiy: O(m+n), O(1)
    # Tip: (a+ib) * (c+id) = (a*c - b*d) + (a*d + b*c)i
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        # Parse the input numbers and extract real and imaginary parts.
        # The parts are separated by a '+'. Also remove the trailing 'i' char.
        real1, imag1 = map(int, num1[:-1].split('+'))
        real2, imag2 = map(int, num2[:-1].split('+'))

        # Compute the real and imaginary components of the product resultant.
        # imag1 * imag2 has -ve coefficient because i^2 = -1.
        res_real = real1 * real2 - imag1 * imag2
        res_imag = real1 * imag2 + real2 * imag1

        # Build the resultant string from its components.
        res = f"{res_real}+{res_imag}i"
        return res
