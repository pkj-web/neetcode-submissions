class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:

        res = []
        nums.sort()
        def dfs(i, cur, total):
            if(total == target): # base case
                res.append(cur.copy())
                return

            for j in range(i, len(nums)):

                #pruning
                if total + nums[j] > target:
                    return

                #try
                cur.append(nums[j])
                #backtrack
                dfs(j, cur, total+nums[j])
                #undo
                cur.pop()

        dfs(0, [], 0)
        return res
            