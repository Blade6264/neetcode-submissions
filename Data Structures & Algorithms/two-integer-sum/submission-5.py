class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # brute force 2 for loops -> time complexity: O(n^2)
        # len_arr = len(nums)
        # for i in range(len_arr):
        #     for j in range(i+1, len_arr):
        #         if nums[i] + nums[j] == target:
        #             return [i, j]
        # return [-1, -1]

        # more efficient way
        # we can make a hashmap with the key: remainder = target - curr_num, 
        # and the value is the index of the curr_num

        # so that when we search if the remainder = curr_num, it's O(1) for time complexity
        # the space complexity will be expensive when using hashmap, which is O(n)
        target_num = {}
        for i in range(len(nums)):
            remainder = target - nums[i]
            if remainder in target_num:
                return [target_num[remainder], i]
            target_num[nums[i]] = i
        # assume if the pair of values isn't in the given list
        print(target_num)
        return [-1, -1]