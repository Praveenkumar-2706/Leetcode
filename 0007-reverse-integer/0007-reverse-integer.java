class Solution {
    public int reverse(int x) {
        // Step 1: Get the sign
        int sign = x < 0 ? -1 : 1;

        // Step 2: Convert absolute value to string
        String str = new StringBuilder(String.valueOf(Math.abs((long)x))).reverse().toString();

        // Step 3: Convert back to integer and handle overflow
        try {
            int reversed = Integer.parseInt(str);
            return reversed * sign;
        } catch (NumberFormatException e) {
            // If it overflows
            return 0;
        }
    }
}
