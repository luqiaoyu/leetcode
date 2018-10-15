# 39. Combination Sum

# backtracking, 回溯: 152ms
class Solution:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        result = []
        candidates.sort()
        self.backtrack(candidates, target, result, [], 0)
        return result

    def backtrack(self, candidates, target, result, temp, index):
        if target < 0: 
            return
        elif target == 0:
            result.append(list(temp))
            return
        else:
            for i in range(index, len(candidates)):
                temp.append(candidates[i])
                self.backtrack(candidates, target - candidates[i], result, temp, i)
                temp.pop()

# dp: 64ms
class Solution1:
    def combinationSum(self, candidates, target):
        """
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        dp = [[[]]] + [[] for i in range(target)]
        candidates.sort()
        for t in range(1, target + 1):
            for i in candidates:
                if i > t:
                    break
                else:
                    for temp in dp[t - i]:
                        if not temp or i >= temp[-1]:
                            dp[t] += temp + [i],    # 一定要有这个逗号！不知道为什么，否则会报错
        return dp[target]

