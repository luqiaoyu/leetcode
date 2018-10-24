# 49. Group Anagrams

import collections

# Categorize by sorted string
# setdefault
# leetcode会报错
# 用''' '''里的OK: 124ms
class Solution:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        d = {}
        for x in strs:
            d.setdefault(tuple(sorted(x)), []).append(x)    # sorted返回list，不可哈希，要转为tuple
        result = d.values()
        '''
        for _, value in d.items():
            result.append(value)
        '''
        return result

# Categorize by sorted string
# collections.defaultdict
# leetcode会报错
class Solution1:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        d = collections.defaultdict(list)
        for x in strs:
            d[tuple(sorted(x))].append(x)    # sorted返回list，不可哈希，要转为tuple
        result = d.values()
        return result

# Categorize by Count: 136ms
class Solution2:
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        result = []
        d = {}
        for x in strs:
            count = [0] * 26
            for i in x:
                count[ord(i) - ord('a')] += 1
            d.setdefault(tuple(count), []).append(x)
        for _, value in d.items():
            result.append(value)
        return result