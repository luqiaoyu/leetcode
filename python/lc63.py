# 63. Unique Paths II

# 44ms 45.40% O(m * n)
class Solution:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        # m行n列
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        d = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 1:
            return 0
        else:
            d[0][0] = 1
        for i in range(1, m):
            if obstacleGrid[i][0] == 1:
                d[i][0] = 0
            else:
                d[i][0] = d[i - 1][0]
        for j in range(1, n):
            if obstacleGrid[0][j] == 1:
                d[0][j] = 0
            else:
                d[0][j] = d[0][j - 1]
        for i in range(1, m):
            for j in range(1, n):
                if obstacleGrid[i][j] == 1:
                    d[i][j] = 0
                else:
                    d[i][j] = d[i - 1][j] + d[i][j - 1]
        return d[-1][-1]

# 差不多
class Solution1:
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """
        m = len(obstacleGrid)
        n = len(obstacleGrid[0])
        d = [[0] * n for _ in range(m)]
        if obstacleGrid[0][0] == 0:
            d[0][0] = 1
        else:
            return 0
        for i in range(1, m):
            d[i][0] = d[i - 1][0] if obstacleGrid[i][0] == 0 else 0
        for j in range(1, n):
            d[0][j] = d[0][j - 1] if obstacleGrid[0][j] == 0 else 0
        for i in range(1, m):
            for j in range(1, n):
                d[i][j] = d[i - 1][j] + d[i][j - 1] if obstacleGrid[i][j] == 0 else 0
        return d[-1][-1]