class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        # stack = [9]
        for s in tokens:

            if s == "+":

                x = int(stack.pop())
                y = int(stack.pop())

                stack.append(x+y)

            elif s== "-":

                x = int(stack.pop())
                y = int(stack.pop())

                stack.append(y-x)
            
            elif s=="*":
                x = int(stack.pop())
                y = int(stack.pop())

                stack.append(y*x)
            

            elif s=="/":

                x = int(stack.pop())
                y = int(stack.pop())

                stack.append(int(y/x))
            

            else:
                stack.append(int(s))


        return stack[-1]