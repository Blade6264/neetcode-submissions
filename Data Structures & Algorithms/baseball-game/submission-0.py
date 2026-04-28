class Solution:
    def calPoints(self, operations: List[str]) -> int:
        result = []
        for operation in operations:
            if operation == "D":
                result.append(result[-1] * 2)
            elif operation == "C":
                result.pop()
            elif operation == "+":
                result.append(result[-1] + result[-2])
            else:
                result.append(int(operation))
        ans = 0
        for num in result:
            ans += num
        return ans
        

