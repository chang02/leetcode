from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        idx = 0
        sortedIntervals = sorted(intervals, key = lambda x: x[0])
        while True:
            if len(sortedIntervals[idx:]) < 2:
                break
            if sortedIntervals[idx][1] >= sortedIntervals[idx+1][0]:
                newInterval = [sortedIntervals[idx][0], max(sortedIntervals[idx+1][1], sortedIntervals[idx][1])]
                del sortedIntervals[idx]
                del sortedIntervals[idx]
                sortedIntervals.insert(idx, newInterval)
                continue
            else:
                idx += 1
                continue
        return sortedIntervals