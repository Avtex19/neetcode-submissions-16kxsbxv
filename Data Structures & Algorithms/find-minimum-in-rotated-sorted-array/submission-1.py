class Solution:
    def findMin(self, nums: List[int]) -> int:
        minEl = nums[0]
        for i in nums:
            minEl = min(minEl,i)
        return minEl

        



        