class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        remainder = []
        # brute force 2 for loops -> time complexity: O(n^2)
        len_arr = len(nums)
        for i in range(len_arr):
            for j in range(i+1, len_arr):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return [-1, -1]