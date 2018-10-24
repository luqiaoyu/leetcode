# 49. Group Anagrams

import collections

# Categorize by sorted string
# setdefault
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
        result = list(d.values())   # 注意.values()返回的数据类型不是list，要转化为list
        '''
        for _, value in d.items():
            result.append(value)
        '''
        return result

# Categorize by sorted string
# collections.defaultdict
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
        result = list(d.values())   # 注意.values()返回的数据类型不是list，要转化为list
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