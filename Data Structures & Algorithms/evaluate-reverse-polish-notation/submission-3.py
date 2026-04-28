class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        operations = {
            "+": lambda x, y: x + y,
            "-": lambda x, y: x - y,
            "*": lambda x, y: x * y,
            "/": lambda x, y: x / y,
        }
        result_stack = []
        for op in tokens:
            # if op.isdigit():
            #     # note to myself: if the str contains '-' to represent neg number
            #     # then that string will return false for .isdigit()
            #     # ex: a = '-11' a.isdigit() -> False
            #     result_stack.append(int(op))
            # else:

            # round to zero -> use int()
            if op in operations:
                result = int(operations[op](result_stack[-2], result_stack[-1]))
                result_stack.pop()
                result_stack.pop()
                result_stack.append(result)
                print(result)
            else:
                result_stack.append(int(op))

        return result_stack[0]