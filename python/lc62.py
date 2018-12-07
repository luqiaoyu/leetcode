# 62. Unique Paths

import math

# 60ms 12.82% O(m*n) DP
class Solution:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m <= 1 or n <= 1:
            return 1

        D = [[0] * n for _ in range(m)]
        for i in range(m):
            for j in range(n):
                if i == 0 or j == 0:
                    D[i][j] = 1
                else:
                    D[i][j] = D[i - 1][j] + D[i][j - 1]

        return D[m - 1][n - 1]

# 可以优化空间复杂度，只存两列（前一列和当前一列，O(min(m, n))）或者一列（直接在前一列上更新，O(min(m, n))），时间复杂度O(m * n)
# 72ms 5.88%
class Solution1:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        if m < n:
            return self.uniquePaths(n, m)

        cur = [1] * n
        for _ in range(1, m):   # 注意循环起点
            for i in range(1, n):   # 注意循环起点
                cur[i] += cur[i - 1]

        return cur[n - 1]   # cur[-1] 更快

# 36ms 94.37%
class Solution1_1:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        cur = [1] * n
        for _ in range(1, m):
            for j in range(1, n):
                cur[j] += cur[j - 1]

        return cur[-1]

# 从数学角度求解，答案为m + n - 2取m - 1
# 72ms
class Solution2:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        N = m + n - 2
        k = min(m, n) - 1
        up = 1
        down = 1
        for i in range(1, k + 1):
            up = up * (N - k + i)
            down = down * i
        return up // down

# 72ms
class Solution3:
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """
        return math.factorial(m + n - 2) // (math.factorial(m - 1) * math.factorial(n - 1))