class Solution:

    def encode(self, strs: List[str]) -> str:

        x = []

        for i in strs:
            x.append(str(len(i)))
            x.append("#")
            x.append(i)

        return "".join(x)

    def decode(self, s: str) -> List[str]:

        y = []

        i = 0

        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            
            length = int(s[i:j])
            i = j + 1
            j = length + i
            
            

            y.append(s[i:j])

            i = j

        return y

        
        
            

            

        


