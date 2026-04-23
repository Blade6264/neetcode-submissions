class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = {}
        for i in range(len(nums)):
            remainder[i] = target - nums[i]
            if remainder[i] in nums and nums.index(remainder[i]) != i:
                if (i < nums.index(remainder[i])):
                    return [i, nums.index(remainder[i])]
                return [nums.index(remainder[i]), i]