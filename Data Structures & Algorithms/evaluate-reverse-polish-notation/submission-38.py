class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = [] 
        # stack = []



        for i in tokens:

            if i == "+":
                x = int(stack.pop())
                y = int(stack.pop())

                z = x + y

                stack.append(z)

            elif i == "-":
                x = int(stack.pop())
                y = int(stack.pop())

                z = y-x

                stack.append(z)

            elif i =="*":
                x = int(stack.pop())
                y = int(stack.pop())

                z = x*y

                stack.append(z)

            elif i == "/":
                x = int(stack.pop())
                y= int(stack.pop())

                z = y / x

                stack.append(int(z))
            


           
            

            else:
                stack.append(int(i))


        return stack[-1]


        