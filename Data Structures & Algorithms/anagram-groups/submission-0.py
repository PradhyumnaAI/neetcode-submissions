class Solution:
    def groupAnagrams(self, strs):
        ans = {}
        for i in strs :
            count = [0] * 26
            for char in i :
                count[ord(char)-ord('a')] += 1
            
            key = tuple(count)
            if key not in ans :
                ans[key] = []
            
            ans[key].append(i)
        return list(ans.values())
