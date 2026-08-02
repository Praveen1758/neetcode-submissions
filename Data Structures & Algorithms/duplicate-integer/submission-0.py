class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        h=dict()

        for i in nums:
            if i in h.keys():
                return True
            else:
                h[i]=1
        
        return False
