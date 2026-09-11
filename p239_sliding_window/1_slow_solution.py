"""
Thoughts: 
- Remember that syntax for sliding window. 
- Remember why -1/+1 is needed. Actually unclear on why the +1
"""
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        outs = []
        for i in range(len(nums) - k + 1):
            window = nums[i:i+k]
            outs.append(max(window))
        return outs
