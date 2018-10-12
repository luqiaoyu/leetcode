# 36. Valid Sudoku

class Solution:
    def isValidSudoku(self, board):
        """
        :type board: List[List[str]]
        :rtype: bool
        """
        d = {}
        for i in range(9):
            for j in range(9):
                if board[i][j] == '.': # 注意二维list的取值方式
                    continue
                elif board[i][j] in d:
                    for index in d[board[i][j]]:
                        if index[0] == i or index[1] == j or (index[0] // 3 == i // 3 and index[1] // 3 == j // 3): # 注意
                            return False
                    d[board[i][j]].append((i, j)) # 注意这里的缩进
                else:
                    d[board[i][j]] = [(i, j)]
        return True