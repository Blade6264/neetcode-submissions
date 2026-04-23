class Solution:
    def isPalindrome(self, s: str) -> bool:
        newstr = ""
        s = s.lower().strip()
        for c in s:
            if c.isalpha() or c.isdigit():
                newstr += c
        i = 0
        j = -1
        for a in range(len(newstr)):
            if newstr[i] != newstr[j]:
                return False
            i += 1
            j -= 1
        return True