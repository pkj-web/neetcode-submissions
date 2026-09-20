class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        # Input: tokens = ["1","2","+","3","*","4","-"]

        # Output: 5

        # Explanation: ((1-2)*3)-4 = 5

        # 1 2 3 4 

        stack =[]

        # 1 2

        # 3

        # 9 4 

        result = 0
        

        for i in range(len(tokens)):
            if(tokens[i].isdigit() or tokens[i].lstrip('-').isdigit()
):
                stack.append(int(tokens[i]))
            elif (tokens[i]=="+"):
                y = stack.pop() # 2
                x = stack.pop() # 1
                result = x + y
                stack.append(result)
            elif (tokens[i]=="-"):
                y = stack.pop() # 4
                x = stack.pop() # 9
                result = x - y
                stack.append(result)
            elif (tokens[i]=="*"):
                y = stack.pop() # 3
                x = stack.pop() # 3
                result = x * y # 9
                stack.append(result)
            elif (tokens[i]=="/"):
                y = stack.pop() # 
                x = stack.pop() # 
                result = int(x / y)
                stack.append(result)
           






        return stack[-1]


            

    

            

        

        