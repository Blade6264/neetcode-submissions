class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        nums.sort()
        for i in range(1, len(nums)):
            # if the prev number is the same like the one in front
            # then it contains duplicatation => return true
            if nums[i - 1] == nums[i]:
                return True
        
        return False