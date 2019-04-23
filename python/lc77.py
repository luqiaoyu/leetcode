# 77. Combinations
# 25.4%
class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        res = []
        self.dfs(1, k, [], res, n, k)
        return res

    def dfs(self, cur, left, temp, res, n, k):
        # 终止条件
        if left < 0:
            return

        if left == 0:
            res.append(list(temp))

        for i in range(cur, n + 1):
            temp.append(i)
            self.dfs(i + 1, left - 1, temp, res, n, k)
            temp.pop()

