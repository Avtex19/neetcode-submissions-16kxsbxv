class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        #O(nxlogm)
        l = 1
        r = max(piles)
        speed = r

        while l <= r:
            mid = (l+r)//2

            totalTime = 0
            for p in piles:
                totalTime += -(-p // mid)
            if totalTime <= h:
                speed = mid
                r = mid - 1
            else:
                l = mid+1
        return speed

        
            

