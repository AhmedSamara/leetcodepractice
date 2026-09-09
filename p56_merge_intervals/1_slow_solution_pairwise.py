"""
Thoguhts:
- Remember to use itertools.pairwise for sliding windows. (pythonic)
- handling the case for len == 1. Need to be careful.
- Remember to use a buffer, building as you go causes problems.
    ie: multiple intervals merged.
- Keep the logic of "overlap" in mind. Ex: The "max" line.
"""
from itertools import pairwise

class Solution:

    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if len(intervals) == 1:
            return [intervals[0]]
        intervals.sort(key=lambda x: x[0])
        merged_intervals = []
        new_interval = [-1, -1]
        for (s1, e1), (s2, e2) in pairwise(intervals):
            if new_interval[0] == -1:
                new_interval = [s1, e1]
            # check if the new_interval needs to be updated
            if s2 <= new_interval[1]:
                new_interval[1] = max(new_interval[1], e2)
            else:
                merged_intervals.append(new_interval)
                new_interval = [s2, e2]
        merged_intervals.append(new_interval)
        return merged_intervals
