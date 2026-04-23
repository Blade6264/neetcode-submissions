class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        results = []
        for i in range(len(nums)):
            if i < (len(nums) - 1):
                for j in range(i + 1, len(nums)):
                    if j < (len(nums) - 1):
                        for k in range(j + 1, len(nums)):
                            if nums[i] + nums[j] + nums[k] == 0:
                                temp = sorted([nums[i], nums[j], nums[k]])
                                if temp not in results:
                                    results.append(temp)
        return results