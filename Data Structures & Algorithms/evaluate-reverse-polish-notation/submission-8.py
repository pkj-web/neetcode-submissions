class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        """
        Input: tokens = ["1","2","+","3","*","4","-"]

        Output: 5

        Explanation: ((1 + 2) * 3) - 4 = 5
        """
        
        stack = [3,3]
        

        for i in range(len(tokens)):
            if tokens[i] == "+":
                x = stack.pop()
                y = stack.pop()
                result = int(x)+int(y)
                stack.append(result)
            elif tokens[i]=="*":
                x = stack.pop()
                y = stack.pop()
                result = int(x) * int(y)
                stack.append(result)
            elif tokens[i] == "-":
                x = stack.pop()
                y = stack.pop()
                result = int(y)-int(x)
                stack.append(result)
            elif tokens[i] == "/":
                x = stack.pop()
                y = stack.pop()
                result = int(y) / int(x)
                stack.append(int(result))



            else:

                stack.append(int(tokens[i]))
        return stack[-1]

        