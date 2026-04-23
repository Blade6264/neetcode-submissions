class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        max_result = 0
        current = 0
        for num in nums:
            if num == 1:
                current += 1
            else:
                if max_result < current:
                    max_result = current
                current = 0
        if max_result < current:
            return current
        return max_result