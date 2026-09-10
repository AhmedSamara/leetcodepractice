""" 
- merged[-1] is the buffer itself, instead of a buffer var. 
- intervals[0] instead of [-1,-1] as sentinel, no need to check inside loop.
- begin from intervals[1:] to start from second.
- No need for pairwise because accumulated buffer
   
"""

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort(key=lambda x: x[0])
        
        merged = [intervals[0]]
        for start, end in intervals[1:]:
            if start <= merged[-1][1]:
                merged[-1][1] = max(merged[-1][1], end)
            else:
                merged.append([start, end])
        
        return merged
