package lc56;

import java.util.*;

/**
 * Definition for an interval.
 */
class Interval {
     int start;
     int end;
     Interval() { start = 0; end = 0; }
     Interval(int s, int e) { start = s; end = e; }
 }


/**
 * Created by luqiaoyu on 2018/11/6.
 * 56. Merge Intervals
 * 19ms 63.11%
 * O(nlogn)
 */
public class Solution {
    public List<Interval> merge(List<Interval> intervals) {
        Collections.sort(intervals, new IntervalComparator());

        LinkedList<Interval> res = new LinkedList<>();
        for (Interval x : intervals) {
            if (res.isEmpty() || res.getLast().end < x.start)    // 只有LinkedList才有getLast()方法
                res.add(x);
            else
                res.getLast().end = Math.max(res.getLast().end, x.end);
        }

        return res;
    }
}

class IntervalComparator implements Comparator<Interval> {
    @Override
    public int compare(Interval a, Interval b) {
        return a.start < b.start ? -1 : a.start == b.start ? 0 : 1;
    }
}
