class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}  # key: number, value: index

        for i, num in enumerate(nums):
            remainder = target - num
            
            if remainder in seen:
                return sorted([seen[remainder] , i])
            
            seen[num] = i
        return [0, 0]