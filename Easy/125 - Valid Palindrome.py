class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == " ":
            return True
        s = ''.join(filter(str.isalnum, list(s.lower())))
        return s == s[::-1]
