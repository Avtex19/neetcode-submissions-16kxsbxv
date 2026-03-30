class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        if len(tokens) == 1:
            return int(tokens[0])

        for i in tokens:
            if i not in "+-*/":
                stack.append(i)
            else:
                x = int(stack.pop())
                y = int(stack.pop())
                if i == '+':
                    result = x+y
                elif i == '-':
                    result = y - x 
                elif i == '*':
                    result = x*y

                elif i == '/':
                   result = int(y/x)
                stack.append(result)
                print(stack)
                
        return stack[0]





        