class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        j =1
        for i in range(n):
            for j in range (1,n):
                if(i != j):
                    sum = nums [i]+ nums[j]
                    if(sum ==target ):
                        return [i,j]
                