# 48. Rotate Image

# 旋转中心点坐标（index）为(x_0, x_0)，
# 确认旋转矩阵后可得旋转前坐标与旋转后坐标关系，
# x2 = y1, y2 = - x1 + 2 * x0
# x1 = - y2 + 2 * x0, y1 = x2
# 逐层旋转
# 48ms
class Solution:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        n = len(matrix)
        i = 0
        while(i != n // 2):    # 注意层数
            self.rotatei(matrix, i)
            i += 1
        
    def rotatei(self, matrix, i):
        n = len(matrix)
        mx0 = (n - 1)
        for j in range(i, n - i - 1):    # 注意起点和终点
            x2, y2 = i, j
            x1, y1 = - y2 + mx0, x2
            temp = matrix[x2][y2]    # 注意二维list取值的方式
            while((x1, y1) != (i, j)):
                matrix[x2][y2] = matrix[x1][y1]    # 注意不要写反
                x2, y2 = x1, y1
                x1, y1 = - y2 + mx0, x2
            matrix[x2][y2] = temp

# 顺时针旋转矩阵，等价于先上下翻转，再取转置
# 逆时针旋转矩阵，等价于先左右翻转，再取转置
# 36ms
class Solution1:
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """
        matrix.reverse()
        n = len(matrix)
        for i in range(n):
            for j in range(i + 1, len(matrix[i])):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]


