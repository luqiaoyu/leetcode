# 6. ZigZag Conversion

# Sort by Row
# O(n) O(n)
# 108ms 61.13%
class Solution:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if (n <= numRows or numRows == 1): return s
        zigzag = ['' for i in range(numRows)]
        curRow = 0
        downFlag = False
        for c in s:
            zigzag[curRow] += c
            if (curRow == 0 or curRow == numRows - 1):
                downFlag = not downFlag
            curRow = curRow + 1 if downFlag else curRow - 1
        res = ''.join(zigzag)
        return res

# Visit by Row
# O(n)
# 120ms 50.66%
class Solution1:
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        n = len(s)
        if (n <= numRows or numRows == 1): return s
        
        cycleLen = 2 * (numRows - 1)
        res = ''
        for i in range(numRows):
            j = 0
            while(j + i < n):
                res += s[j + i]
                if (i != 0 and i != numRows - 1 and j + cycleLen - i < n):
                    res += s[j + cycleLen - i]
                j += cycleLen
        return res

        