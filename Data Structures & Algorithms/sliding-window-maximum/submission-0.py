from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()  # stores indices
        result = []
    
        for i, num in enumerate(nums):
            # 1. Remove indices outside the current sliding window
            if dq and dq[0] <= i - k:
                dq.popleft()
            
            # 2. Remove smaller values from the back as they won't be needed
            while dq and nums[dq[-1]] <= num:
                dq.pop()
            
            # 3. Add current element's index
            dq.append(i)
        
            # 4. Append max to output array once we reach first window of size k
            if i >= k - 1:
                result.append(nums[dq[0]])
            
        return result