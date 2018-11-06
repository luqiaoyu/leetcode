# 56. Merge Intervals

# Definition for an interval.
class Interval:
    def __init__(self, s=0, e=0):
        self.start = s
        self.end = e

# 80ms 33.12%
# O(nlogn)
class Solution:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n <= 1: return intervals
        sort_i = sorted(intervals, key = lambda x : x.start)
        result = []
        result.append(sort_i[0])
        for i in range(1, n):
            if result[-1].end >= sort_i[i].start:
                result[-1].end = max(result[-1].end, sort_i[i].end)
                continue
            else:
                result.append(sort_i[i])
        return result

# 64ms 87.08%
# O(nlogn)
class Solution1:
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """
        n = len(intervals)
        if n <= 1: return intervals
        intervals.sort(key = lambda x : x.start)    # in-place sort会快一点？
        result = []
        result.append(intervals[0])
        for i in range(1, n):
            if result[-1].end >= intervals[i].start:
                result[-1].end = max(result[-1].end, intervals[i].end)
                continue
            else:
                result.append(intervals[i])
        return result

