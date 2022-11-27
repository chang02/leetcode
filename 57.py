from typing import List

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if len(intervals) == 0:
            return [newInterval]
        
        idx = 0
        poped = []
        while idx < len(intervals):
            if newInterval[0] > intervals[idx][1]:
                idx += 1
                continue
            elif newInterval[1] < intervals[idx][0]:
                break
            else:
                poped.append(intervals[idx])
                del intervals[idx]
                continue
        intervals.insert(idx, self.mergeSortedIntervals(poped, newInterval))
        return intervals
            
    def mergeSortedIntervals(self, intervals, newInterval):
        if len(intervals) == 0:
            return newInterval
        f = min(intervals[0][0], newInterval[0])
        t = max(intervals[-1][1], newInterval[1])
        return [f, t]

s = Solution()
print(s.insert([[1,3],[6,9]], [2,5]))