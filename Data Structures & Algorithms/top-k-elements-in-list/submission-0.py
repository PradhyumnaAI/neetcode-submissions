class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}

        
        for item in nums:
            if item in freq:
                freq[item] += 1
            else:
                freq[item] = 1

        
        sorted_items = sorted(freq.items(), key=lambda x: x[1], reverse=True)

        output = []
        
        for key, value in sorted_items:
            output.append(key)
            if len(output) == k:
                break

        return output