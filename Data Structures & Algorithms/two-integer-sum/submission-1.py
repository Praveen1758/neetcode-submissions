class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        h = {}

        # First pass
        for i in range(len(nums)):
            h[nums[i]] = i

        # Second pass
        for i in range(len(nums)):
            diff = target - nums[i]

            if diff in h and h[diff] != i:
                return [i, h[diff]]