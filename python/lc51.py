# 51. N-Queens

# backtracking
# 248ms
class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """
        result = []
        temp = [0] * n
        self.backtrack(0, n, result, temp)
        return result

    def backtrack(self, row, n, result, temp):
        if (row == n):
            result.append(['.' * x + 'Q' + '.' * (n - x - 1) for x in temp])
        else:
            for col in range(n):
                temp[row] = col
                if (self.isVal(row, n, temp)):
                    self.backtrack(row + 1, n, result, temp)

    # 检验第row行的放置是否有效
    def isVal(self, row, n, temp):
        for j in range(row):
            if (temp[j] == temp[row] or j + temp[j] == row + temp[row] or temp[j] - j == temp[row] - row):
                return False
        return True