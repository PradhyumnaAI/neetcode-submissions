class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = sorted(nums)
        flag = False
        for i in range (len(nums)-1):
            if (arr[i]== arr[i+1] and (i+1) <= len(arr)):
                flag = True 
                break 
            
        return flag

        
        