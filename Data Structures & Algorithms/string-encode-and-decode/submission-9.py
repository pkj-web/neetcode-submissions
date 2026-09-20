class Solution:

    def encode(self, strs: List[str]) -> str:

        array=[]

        for i in strs:
            array.append(str(len(i)))
            array.append("#")
            array.append(i)

        return "".join(array)


    def decode(self, s: str) -> List[str]:

        array = []

        i = 0

        while i < len(s):
            j=i
            while s[j] != "#":
                j+=1
            

            length=int(s[i:j])

            i = j+1
            j = i + length

            array.append(s[i:j])

            i=j

        return array

