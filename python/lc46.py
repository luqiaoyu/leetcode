# 46. Permutations

# backtracking: 52ms
class Solution:
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        result = []
        self.backtrack(result, [], nums)
        return result

    def backtrack(self, result, temp, nums):
        if (len(temp) == len(nums)):
            result.append(list(temp))
        else:
            for x in nums:
                if (x not in temp):
                    temp.append(x)
                    self.backtrack(result, temp, nums)
                    temp.pop()