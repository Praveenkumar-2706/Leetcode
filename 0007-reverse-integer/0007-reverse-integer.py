class Solution(object):
    def reverse(self, x):
        max_val = (2 ** 31) - 1
        sign = -1 if x < 0 else 1
        x = abs(x)
        rev = 0
        while x != 0:
            digit = x % 10
            x /= 10
            rev = rev * 10 + digit
            if rev > (max_val-digit/10):
                return 0

        return rev*sign

        