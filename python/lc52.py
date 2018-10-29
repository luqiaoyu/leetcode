# 52. N-Queens II

# backtracking
# 136ms
class Solution:
    def totalNQueens(self, n):
        """
        :type n: int
        :rtype: int
        """
        self.result = 0    # !!! use global variable
        temp = [0] * n
        self.backtrack(0, n, temp)
        return self.result

    def backtrack(self, row, n, temp):
        if (row == n):
            self.result += 1
        else:
            for col in range(n):
                temp[row] = col
                if (self.isVal(row, n, temp)):
                    self.backtrack(row + 1, n, temp)

    # 检验第row行的放置是否有效
    def isVal(self, row, n, temp):
        for j in range(row):
            if (temp[j] == temp[row] or j + temp[j] == row + temp[row] or temp[j] - j == temp[row] - row):
                return False
        return True