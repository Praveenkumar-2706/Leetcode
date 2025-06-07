class Solution {
    public String convert(String s, int numRows) {
           if (numRows == 1) {
            return s;
        }

        StringBuilder[] rows = new StringBuilder[numRows];
        for (int i = 0; i < numRows; i++) {
            rows[i] = new StringBuilder();
        }

        int add = 0;
        int inc = 1;

        for (char c : s.toCharArray()) {
            rows[add].append(c);
            if (add == 0) {
                inc = 1;
            } else if (add == numRows - 1) {
                inc = -1;
            }
            add += inc;
        }

        StringBuilder result = new StringBuilder();
        for (StringBuilder row : rows) {
            result.append(row);
        }

        return result.toString();
    }
}