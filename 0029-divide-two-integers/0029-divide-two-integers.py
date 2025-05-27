class Solution(object):
    def divide(self, dividend, divisor):

        # Handle overflow case
        if dividend == -2**31 and divisor == -1:
            return 2**31 - 1  # Clamp to INT_MAX

        # Determine the sign of the result
        negative = (dividend < 0) != (divisor < 0)

        # Work with absolute values and convert to long
        dividend, divisor = abs(dividend), abs(divisor)

        result = 0

        while dividend >= divisor:
            temp = divisor
            multiple = 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            dividend -= temp
            result += multiple

        return -result if negative else result
