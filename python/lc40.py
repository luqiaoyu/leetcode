# 40. Combination Sum II

# backtrack: 100ms
class Solution:
    def combinationSum2(self, candidates, target):
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
        if target < 0: return
        elif target == 0:
            '''
            for x in result:
                if x == temp: return
            '''
            result.append(list(temp))
            return
        else:
            for i in range(index, len(candidates)):
                if(i > index and candidates[i] == candidates[i - 1]): continue # 一定要有i > index, 否则结果不对
                temp.append(candidates[i])
                self.backtrack(candidates, target - candidates[i], result, temp, i + 1)
                temp.pop()

        