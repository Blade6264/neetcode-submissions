class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        i = 0
        j = len(numbers) - 1
        for a in range(len(numbers)):
            remainder = target - numbers[i]
            if numbers[j] > remainder:
                j -= 1
            elif numbers[j] < remainder:
                i += 1
            else:
                return [i + 1, j + 1]
        return [0, 0]