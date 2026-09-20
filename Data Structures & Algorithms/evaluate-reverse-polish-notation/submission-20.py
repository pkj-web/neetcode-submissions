class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = [] # 9 4 -


        for i in tokens:
            
            if i == "+":
               x=  int(stack.pop()) #
               y = int(stack.pop())

               stack.append(int(x+y))

            elif i == "-":
                x = int(stack.pop())
                y = int(stack.pop())

                stack.append(int(y-x))



            elif i == "*":
                 x = int(stack.pop())
                 y = int(stack.pop())

                 stack.append(int(x*y))

            elif i == "/":
                x = int(stack.pop())
                y = int(stack.pop())

                stack.append(int(y/x))


            else:
                stack.append(int(i))
             
        return stack[-1]