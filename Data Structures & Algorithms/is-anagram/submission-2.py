class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # i can make a hashmap to get the char and its frequency from 1 string
        # then, on the other str, i will find if either:
        # 1. the char isn't in the list -> not anagram
        # 2.  i will substract the frequency of a char from the new string and see
        # if the frequency of all char at the end = 0
        # if it isn't 0 -> not anagram
        char_freq = {}
        for c in s:
            if c not in char_freq:
                char_freq[c] = 1
            else:
                char_freq[c] += 1
        for c in t:
            if c not in char_freq:
                return False
            else:
                char_freq[c] -= 1
        return all(value == 0 for value in char_freq.values())