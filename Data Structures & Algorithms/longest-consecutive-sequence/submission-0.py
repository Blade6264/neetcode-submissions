class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if len(nums) == 0:
            return 0
        curr_result = 1
        highest_result = 1
        nums = list(set(nums))
        nums.sort()
        print(nums)
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i + 1]:
                curr_result += 1
            else:
                if curr_result > highest_result:
                    highest_result = curr_result
                curr_result = 1
        if curr_result > highest_result:
            return curr_result
        return highest_result