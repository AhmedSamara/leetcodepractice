"""
Thoguhts:
- last solution was bad because had to recompute a max for every iteration.
- deque instead of queu or lsit. (remember poplegt and pop).
- I overthought start condition (just don't print until first window built).
"""

from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        outs = []
        q = deque()
        for i in range(len(nums)):
            newval = nums[i]

            # check if need to pop front due to age:
            if q and q[0] < i - k+1:
                q.popleft()

            # Pop from the right if a new max has entered:
            while q and nums[q[-1]] < newval:
                q.pop()

            q.append(i)

            if i >= k-1:
                outs.append(nums[q[0]])

        return outs
