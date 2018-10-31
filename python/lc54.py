# 54. Spiral Matrix

# 44ms
class Solution:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if (len(matrix) == 0): return []
        m = len(matrix)
        n = len(matrix[0])
        result = []
        i, j = 0, 0
        edge = 1
        while(len(result) < m * n):
            result.append(matrix[i][j])
            while(j < n - edge):
                j += 1
                result.append(matrix[i][j])
            while(i < m - edge):
                i += 1
                result.append(matrix[i][j])
            if (len(result) == m * n): return result
            while(j > edge - 1):
                j -= 1
                result.append(matrix[i][j])
            while(i > edge):
                i -= 1
                result.append(matrix[i][j])
            j += 1
            edge += 1
        return result

# Simulation
# 36ms
class Solution1:
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix: return []
        R, C = len(matrix), len(matrix[0])
        seen = [[False] * C for _ in matrix]
        ans = []
        dr = [0, 1, 0, -1]
        dc = [1, 0, -1, 0]
        r = c = di = 0
        for _ in range(R * C):
            ans.append(matrix[r][c])
            seen[r][c] = True
            cr, cc = r + dr[di], c + dc[di]    # candidate next position
            if 0 <= cr < R and 0 <= cc < C and not seen[cr][cc]:
                r, c = cr, cc
            else:
                di = (di + 1) % 4
                r, c = r + dr[di], c+ dc[di]
        return ans
