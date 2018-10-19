# 47. Permutations II

# backtracking: 72ms
class Solution:
    def permuteUnique(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        nums.sort()
        used = [False for i in range(len(nums))]
        self.backtrack(result, [], nums, used)
        return result

    def backtrack(self, result, temp, nums, used):
        if (len(temp) == len(nums)):
            result.append(list(temp))
        else:
            for i in range(len(nums)):
                if (used[i] or ((i > 0) and (nums[i] == nums[i - 1]) and (not used[i - 1]))): # 对于连续相同的值，只能顺序加入temp，这样来避免重复
                    continue
                else:
                    used[i] = True
                    temp.append(nums[i])
                    self.backtrack(result, temp, nums, used)
                    used[i] = False
                    temp.pop()
