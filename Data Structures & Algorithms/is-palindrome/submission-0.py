class Solution:
    def isPalindrome(self, s: str) -> bool:
        str1=""
        for ch in s:
            if ch.isalnum():  # method that check if a character is alplanumeric or not
            # meaning letters (a-z), (A-Z) and numbers (0-9).
                str1+=ch.lower()
        
        return str1[::-1]==str1

