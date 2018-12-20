# 64. Minimum Path Sum

# 88ms 26.69% DP O(m * n)
class Solution:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        sum_d = [[0] * n for _ in range(m)]
        sum_d[0][0] = grid[0][0]
        for i in range(1, m):
            sum_d[i][0] = sum_d[i - 1][0] + grid[i][0]
        
        for j in range(1, n):
            sum_d[0][j] = sum_d[0][j - 1] + grid[0][j]

        for i in range(1, m):
            for j in range(1, n):
                sum_d[i][j] = min(sum_d[i - 1][j], sum_d[i][j - 1]) + grid[i][j]

        return sum_d[-1][-1]

# 60ms 66.27%
class Solution1:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])
        dp = grid[0]
        for j in range(1, n):
            dp[j] += dp[j - 1]

        for i in range(1, m):
            dp[0] += grid[i][0]
            for j in range(1, n):
                dp[j] = min(dp[j], dp[j - 1]) + grid[i][j]

        return dp[-1]

# 112ms 11.66%
class Solution2:
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        m = len(grid)
        n = len(grid[0])

        for i in range(1, m):
            grid[i][0] += grid[i - 1][0]
        
        for j in range(1, n):
            grid[0][j] += grid[0][j - 1]

        for i in range(1, m):
            for j in range(1, n):
                grid[i][j] += min(grid[i - 1][j], grid[i][j - 1])

        return grid[-1][-1]