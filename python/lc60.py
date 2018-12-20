# 60. Permutation Sequence

# 超时
class Solution:
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        self.count = 0
        self.res = ''
        temp = ''
        self.backtrack(n, k, temp)
        return self.res

        
    def backtrack(self, n, k, temp):
        if self.count == k:
            return
        if len(temp) == n:
            self.count += 1
            self.res = temp
            return
        for i in range(1, n + 1):
            if str(i) in temp:
                continue
            temp += str(i)
            self.backtrack(n, k, temp)
            temp = temp[:-1]
