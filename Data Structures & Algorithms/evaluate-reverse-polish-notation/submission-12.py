class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = [] #[9,4]
                    #[9]
        for c in tokens:
            if(c == "+"):
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(x+y)

            
            elif(c=="-"):
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(y-x)
            
            elif(c=="*"):
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(x*y)
            
            elif(c=="/"):
                x = int(stack.pop())
                y = int(stack.pop())
                stack.append(int(y/x))


            else:
                stack.append(int(c))

        return stack[-1]



            
        