# 59. Spiral Matrix II

# 36ms 99.38%
class Solution:
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """
        if n <= 0: return []

        res = [[0] * n for i in range(n)]
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for x in range(1, n ** 2 + 1):
            res[r][c] = x
            cr, cc = r + dr[di], c + dc[di]
            if (0 <= cr < n and 0 <= cc < n and res[cr][cc] == 0):
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c + dc[di]
        
        return res