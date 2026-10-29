class Solution:
    def isValid(self, s: str) -> bool:
        # lock in bro

        valid = { "]":"[", ")": "(", "}":"{" } # this are the valid options only

        stack = []
        for i in s:
            if i in valid:
                if stack and stack[-1]==valid[i]:
                    stack.pop()

                else:
                    return False



            else:
                stack.append(i)


        

        return True if not stack else False

        '''
        s= "[]"
        stack = [  "["               ]
        '''
        