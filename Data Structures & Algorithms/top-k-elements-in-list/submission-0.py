class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        my_dict = {}
        for i in nums:
            my_dict[i] = my_dict.get(i,0)+1        
        top_k = sorted(my_dict, key=my_dict.get, reverse=True)[:k]
        return top_k
    
