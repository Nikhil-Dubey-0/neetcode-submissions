class Solution:
    def isPalindrome(self, s: str) -> bool:

        string=""

        for c in s:
            if c.isalnum():
                string+=c.lower()

        j = len(string)-1

        for i in range(len(string)):
            if string[i]!=string[j]:
                return False

            j-=1
        return True