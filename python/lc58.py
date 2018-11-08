# 58. Length of Last Word

# split
# 32ms 100%
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0
        
        res = 0
        array = s.split(' ')
        n = len(array)
        for i in range(n - 1, -1, -1):
            if array[i] != '':
                res = len(array[i])
                break
        return res

# 36ms
class Solution1:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return 0

        res = 0
        n = len(s)
        for i in range(n - 1, -1, -1):
            if res == 0:
                if s[i] == ' ':
                    continue
                else:
                    res += 1
            else:
                if s[i] == ' ':
                    break
                else:
                    res += 1

        return res

# 40ms
class Solution2:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """
        return len(s.rstrip(' ').split(' ')[-1])