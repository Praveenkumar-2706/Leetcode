public class Solution {
    public boolean isPalindrome(int x) {
        // beacause Negative numbers are not palindromes
        if (x < 0) {
            return false;
        }
        
        // Convert Integer number to string
        String str = Integer.toString(x);
        
        // Reverse the string
        String reversed = new StringBuilder(str).reverse().toString();
        
        // Compare original and reversed, if equal then it is palindrome else not a palindrome
        return str.equals(reversed);
    }
}
