class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        arr = sorted(nums)
        flag = False
        for i in range (len(nums)):
            if ((i+1) < len(arr) and arr[i]== arr[i+1] ):
                return True 
                
            
        return False

        
        