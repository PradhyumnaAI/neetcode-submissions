class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        dict1 = {}
        for index,value in enumerate (nums):
            num1 = target - value 
            if num1 in dict1:
                return [dict1[num1],index]
            else :
                dict1 [value]= index
                