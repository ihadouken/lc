class Solution:
    def fractionToDecimal(self, numerator: int, denominator: int) -> str:
        # Decimal equals zero if numerator equals 0.
        if not numerator:
            return '0'

        # Check if decimal is +ve or -ve.
        if (numerator < 0) ^ (denominator < 0):
            ans = '-'
        else:
            ans = ''

        # Negative input has already been accounted for so use absolute inputs.
        numerator = abs(numerator)
        denominator = abs(denominator)

        # Find integral part of the decimal.
        ans += str(numerator // denominator)

        # Check if there will be digits after decimal place.
        rem = numerator % denominator
        if not rem:
            return ans
        ans += '.'

        seen_rem = {}
        while rem:
            # Remember remainder and the place of the quotient obtained when the
            # remainder is further divided. If the remainder repeats itself then
            # the quotient will start repeating itself too. Return the substring
            # of repeating quotient within parenthesis in the final result.
            if rem in seen_rem:
                return ans[:seen_rem[rem]] + '(' + ans[seen_rem[rem]:] + ')'

            # The quotient obtained when the remainder is divided is yet to be
            # added.
            seen_rem[rem] = len(ans)

            # Calculate the quotient due to the remainder and append it to ans.
            rem *= 10
            ans += str(rem // denominator)

            # Find the next remainder.
            rem %= denominator
        return ans
