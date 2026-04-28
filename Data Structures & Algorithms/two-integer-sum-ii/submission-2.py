class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        for i in range(len(numbers)):
            num_need = target - numbers[i]
            for j in range(i, len(numbers)):
                if num_need == numbers[j]:
                    return [i+1, j+1]
