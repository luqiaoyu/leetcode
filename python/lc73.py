# 73. Set Matrix Zeroes

# time O(mn); space O(m + n)
# 136ms 32.18%
class Solution:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)    # num of rows
        n = len(matrix[0])    # num of columns
        
        r = set()
        c = set()
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    r.add(i)
                    c.add(j)

        for x in r:
            for j in range(n):
                matrix[x][j] = 0
        
        for y in c:
            for i in range(m):
                matrix[i][y] = 0

# time O(mn(m + n)); space O(1)
# 168ms 18.94%
class Solution1:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.setRowX(matrix, m, n, i)
                    self.setColX(matrix, m, n, j)
        
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'x':
                    matrix[i][j] = 0

    def setRowX(self, matrix, m, n, i):
        for j in range(n):
            if matrix[i][j] == 0:
                continue
            else:
                matrix[i][j] = 'x'

    def setColX(self, matrix, m, n, j):
        for i in range(m):
            if matrix[i][j] == 0:
                continue
            else:
                matrix[i][j] = 'x'

# 152ms 25.02%
class Solution2:
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        m = len(matrix)
        n = len(matrix[0])

        flag_c0 = False
        
        for i in range(m):
            if matrix[i][0] == 0:
                flag_c0 = True
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[0][j] = 0
                    matrix[i][0] = 0

        for i in range(1, m):
            if matrix[i][0] == 0:
                for j in range(n):
                    matrix[i][j] = 0

        for j in range(1, n):
            if matrix[0][j] == 0:
                for i in range(m):
                    matrix[i][j] = 0

        if matrix[0][0] == 0:
            for j in range(n):
                matrix[0][j] = 0

        if flag_c0:
            for i in range(m):
                matrix[i][0] = 0
            



