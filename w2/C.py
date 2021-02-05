class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        k=0
        for i in range(0,len(nums)):
            for j in range(i,len(nums)):
                if nums[i]==nums[j] and i<j:
                    k+=1
        return k
    
