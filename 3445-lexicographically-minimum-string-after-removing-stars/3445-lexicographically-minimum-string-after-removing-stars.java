import java.util.*;

class Solution {
    public String clearStars(String s) {
        int n = s.length();
        boolean[] remove = new boolean[n];

        Map<Character, Deque<Integer>> charIndices = new HashMap<>();
        for (char c = 'a'; c <= 'z'; c++) {
            charIndices.put(c, new ArrayDeque<>());
        }

        for (int i = 0; i < n; i++) {
            char ch = s.charAt(i);

            if (ch == '*') {
                remove[i] = true;

                for (char c = 'a'; c <= 'z'; c++) {
                    if (!charIndices.get(c).isEmpty()) {
                        int indexToRemove = charIndices.get(c).pop();
                        remove[indexToRemove] = true;
                        break;
                    }
                }

            } else {
                charIndices.get(ch).push(i);
            }
        }


        StringBuilder result = new StringBuilder();
        for (int i = 0; i < n; i++) {
            if (!remove[i]) {
                result.append(s.charAt(i));
            }
        }

        return result.toString();
    }


    public static void main(String[] args) {
        Solution sol = new Solution();
        String s = "ab*cd*";
        System.out.println(sol.clearStars(s));
    }
}
