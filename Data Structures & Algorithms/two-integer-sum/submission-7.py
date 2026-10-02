class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        indexed_nums = [(num, i) for i, num in enumerate(nums)]
        indexed_nums.sort(key=lambda x: x[0]) 

        left, right = 0, len(nums) - 1

        while left < right:
            current_sum = indexed_nums[left][0] + indexed_nums[right][0]
            if current_sum == target:
                i1, i2 = indexed_nums[left][1], indexed_nums[right][1]
                return [min(i1, i2), max(i1, i2)]  # Ensures indices are in ascending order
            elif current_sum > target:
                right -= 1
            else:
                left += 1