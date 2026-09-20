class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # lock in mode activated, computer lets go
        stack = []

        for i in tokens:

            if i == "+":
                x = stack.pop()
                y = stack.pop()
                stack.append(x+y)

            elif i == "-":
                x = stack.pop()
                y = stack.pop()
                stack.append(y-x)

            elif i == "*":
                x = stack.pop()
                y = stack.pop()
                stack.append(x*y)

            elif i == "/":
                x = stack.pop()
                y = stack.pop()
                stack.append(int(y/x))

            else:
                stack.append(int(i))

        

        return stack[-1]
        