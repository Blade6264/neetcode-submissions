# [1, 1, 2, 1, 4] val = 1
#  i  j -> arr[j - 1] = arr[j]

# [1, 2, 1, 4]
#  i  j -> arr[j - 1] = arr[j]

# [2, 1, 4]
#  i  j

# [2, 1, 4]
#     i  j

# [2, 1, 4]
#     i  j
class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i = 0
        while i < len(nums):
            if nums[i] == val:
                nums.pop(i)
            else:
                i += 1
        return len(nums)