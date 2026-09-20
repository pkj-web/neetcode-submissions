class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        # Input: numbers = [1,2,3,4], target = 3
        # Output: [1,2]

        left = 0
        right=len(numbers)-1 # 3

        while left < right: # 0<3
            if(numbers[left]+numbers[right] > target):
                right-=1
            if(numbers[left]+numbers[right] < target):
                left+=1
            if(numbers[left]+numbers[right] == target):
                return [left+1,right+1]


            

            


        