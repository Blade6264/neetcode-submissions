class Solution:
    def isValid(self, s: str) -> bool:

        # use a stack
        bracket = []
        open_brackets = ["(", "{", "["]
        close_brackets = [")", "}", "]"]
        for char in s:
            if char in open_brackets:
                bracket.append(char)
            else:
                if len(bracket) == 0:
                    return False
                if open_brackets.index(bracket[-1]) == close_brackets.index(char):
                    bracket.pop()
                else:
                    return False
            
        return len(bracket) == 0