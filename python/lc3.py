# 3. Longest Substring Without Repeating Characters

# sliding window
# 116ms
class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        if (len(s) <= 1): return len(s)
        result = 0
        d = {}
        i = 0
        j = 0
        while(j < len(s)):
            if (s[j] not in d or d[s[j]] < i):
                d[s[j]] = j
                j += 1
            else:
                result = max(result, j - i)
                i = d[s[j]] + 1
                d[s[j]] = j
                j += 1
        result = max(result, j - i)
        return result