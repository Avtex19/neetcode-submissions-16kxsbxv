class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        if len(nums1) > len(nums2):
            nums1, nums2 = nums2, nums1
            
        total = len(nums1) + len(nums2)
        half = (total + 1) // 2
        
        l = 0
        r = len(nums1)

        while l <= r: 
            mid1 = (l + r) // 2
            mid2 = half - mid1

            leftA = nums1[mid1 - 1] if mid1 > 0 else float('-inf')
            rightA = nums1[mid1] if mid1 < len(nums1) else float('inf')
            
            leftB = nums2[mid2 - 1] if mid2 > 0 else float('-inf')
            rightB = nums2[mid2] if mid2 < len(nums2) else float('inf')

            if leftA <= rightB and leftB <= rightA:
                
                if total % 2 != 0:
                    return float(max(leftA, leftB))
                
                else:
                    return (max(leftA, leftB) + min(rightA, rightB)) / 2.0
                    
            elif leftA > rightB:
                r = mid1 - 1
            else:
                l = mid1 + 1

        return 0.0