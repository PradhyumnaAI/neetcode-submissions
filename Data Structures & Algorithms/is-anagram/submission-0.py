class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        string1 = "".join(sorted(s))
        string2 = "".join(sorted(t))
        if (string1 == string2):
            return True

        return False 