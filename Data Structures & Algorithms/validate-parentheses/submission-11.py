class Solution:
    def isValid(self, s: str) -> bool:



        stack = []


        valid = {"}":"{", "]":"[", ")":"(" }

        for n in s:
            if(n in valid):
                if( stack and stack[-1]==valid[n]):
                    stack.pop()

                else:
                    return False

            
            else:
                stack.append(n)

        return True if not stack else False 
        