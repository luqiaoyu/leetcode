# 5. Longest Palindromic Substring

# expand around center: 968ms 
class Solution:
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """
        if (len(s) == 0): return ''
        start, end = 0, 0
        for i in range(len(s)):
            len1 = self.extend(s, i, i)
            len2 = self.extend(s, i, i + 1)
            length = max(len1, len2)
            if (length > end - start):
                start = i - (length - 1) // 2
                end = i + length // 2
        return s[start : end + 1]

    def extend(self, s, left, right):
        while(left >= 0 and right < len(s) and s[left] == s[right]):
            left -= 1
            right += 1
        return right - left - 1