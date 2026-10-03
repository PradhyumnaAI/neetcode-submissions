class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = "".join([char for char in s if char.isalnum() ] )
        newString1 = newString.lower()
        reversedString = newString1[::-1]
        if (newString1 == reversedString):
            return True 
        return False