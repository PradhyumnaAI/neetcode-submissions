class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = {}
        # freq[i] stores numbers that appear exactly 'i' times
        freq = [[] for _ in range(len(nums) + 1)]

        # 1. Count frequencies
        for num in nums:
            count[num] = count.get(num, 0) + 1

        # 2. Map numbers into frequency buckets
        for num, c in count.items():
            freq[c].append(num)

        # 3. Collect top k elements starting from highest frequency bucket
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for num in freq[i]:
                res.append(num)
                if len(res) == k:
                    return res