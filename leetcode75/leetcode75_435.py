'''
435. Non-overlapping Intervals
Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.
'''

def eraseOverlapIntervals(self, intervals):
    """
    :type intervals: List[List[int]]
    :rtype: int
    """
    if len(intervals) <= 1:
        return 0
    intervals.sort(key = lambda x: x[1])
    end, count = intervals[0][0], 0
    for s, e in intervals:
        if s >= end:
            end = e
        else:
            count += 1
    return count
