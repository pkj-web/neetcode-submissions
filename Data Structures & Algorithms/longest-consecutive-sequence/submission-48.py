class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        res = set(nums)
       


        # 2 3 4 4 5 10 20 
        # answer = 4, seems like dupes dont count so maybe we do a lil setttty


        # 2 3 4 5 10 20

        '''
        i = 2
        long = 1
        count = 2
        2 3 4 5 10 20

        '''

        long = 0
        for i in res:
            if (i-1) not in res:
                count = 0

                while (i+count) in res:
                    #long = max(long, count)
                    count+=1
                    long = max(long, count)
                

        return long

        