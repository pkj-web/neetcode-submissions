class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
            
        # 4 13 5
        # 13/ 5 = 2
        # 2 4 
        # 6
        stack = []

        for i in tokens:

            if i == "+":
                x = stack.pop()
                y = stack.pop()

                z = int(x)+(y)

                stack.append(z)
                
            elif i == "-":
                x = stack.pop()
                y = stack.pop()

                z = int(y)-(x)

                stack.append(z)

            elif i == "*":
                x = stack.pop()
                y = stack.pop()

                z = int(x)*(y)

                stack.append(z)

            elif i == "/":

                x = stack.pop()
                y = stack.pop()

                z = (y)/(x)

                stack.append(int(z))
                
            else:
                stack.append(int(i))
        

        return stack[-1]