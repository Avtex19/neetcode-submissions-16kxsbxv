class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        indices = [i for i in range(len(position))]
        indices.sort(key=lambda i: position[i],reverse=True)
        stack = []
        for i in indices:
            time = (target - position[i])/speed[i]
            if not stack or time > stack[-1]:
                stack.append(time)
        return len(stack)



        




        
        