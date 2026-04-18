class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l,r = 0,len(nums)-1

        while l < r:
            m = (l + r) // 2
            if nums[m] > nums[r]:
                print(nums[l],nums[r])
                l = m + 1
            else:
                print(nums[l],nums[r])

                r = m

        pivot = l
        l, r = 0, len(nums) - 1
        if target >= nums[pivot] and target <= nums[r]: # if target is in the right half 
            l = pivot
        else:
            r = pivot - 1
        
        while l <= r:
            m = (l+r)//2
            if nums[m] == target:
                return m
            elif nums[m] > target:
                r = m - 1
            else:
                l = m + 1
            
        return -1


        
            


        