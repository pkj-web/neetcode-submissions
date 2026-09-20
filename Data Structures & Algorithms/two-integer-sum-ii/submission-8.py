class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        left = 0
        right = len(numbers)-1

        
        

        while left < right:
            index1 = numbers[left]
            index2 = numbers[right]
            if index1+index2 == target:
                return [left+1, right+1]


            

            elif index1+index2 > target: #3>3
                right-=1
            
            else:
                left+=1
            
            
            
            
            
            
        