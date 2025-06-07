class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        if numRows == 1:
            return s
        
        add = 0
        inc = 1
        rows = [""]*numRows
        for i in s:
            rows[add] += i
            if add == 0:
                inc = 1
            elif add == numRows - 1:
                inc = -1
            
            add += inc
        return "".join(rows)

        