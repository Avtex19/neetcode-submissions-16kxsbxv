class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        first = {}
        second = {}
        for i in s:
            if i in first.keys():
                first[i] += 1
            else:
                first[i] = 1
        for j in t:
            if j in second.keys():
                second[j] += 1
            else:
                second[j] = 1
        print(first,second)
        if len(first) != len(second):
            return False
        
        for key in first:
            if key not in second or first[key] != second[key]:
                return False
        return True
                    
                
        
        