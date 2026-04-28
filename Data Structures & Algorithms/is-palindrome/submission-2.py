class Solution:
    def isPalindrome(self, s: str) -> bool:
        if len(s) == 1:
            return True
        rev_index = 0
        for i in range(len(s)):
            if s[i].isalnum():
                while rev_index < len(s) and not s[-1 - rev_index].isalnum():
                    rev_index += 1
                print("rev_index:", rev_index)
                print("Length", len(s))
                if s[i].lower() != s[-1 - rev_index].lower() or rev_index == len(s):
                    return False
                else:
                    rev_index += 1
        return True