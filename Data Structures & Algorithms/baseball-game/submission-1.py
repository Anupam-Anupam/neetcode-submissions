class Solution:
    def calPoints(self, operations: List[str]) -> int:
        
        stack = []
        ops = operations

        for i in range(len(ops)):
            if ops[i] == "+":
                stack.append(stack[-1] + stack[-2])
            elif ops[i] == "C":
                stack.pop()

            elif ops[i] == "D":
                stack.append(stack[-1] * 2)

            else:
                stack.append(int(ops[i]))
        res = 0
        for nums in stack:
            res += nums

        return res