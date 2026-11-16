class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:

        stack = []
        res = []

        for char in s:
            if char == "(":
                stack.append(")")

            elif char == ")" and stack:
                stack.pop()


            elif char == ")" and len(stack) == 0:
                continue 

            res.append(char)


        i = 0
        n = len(stack)
        s = str(''.join(res))
        j = len(s) - 1
        while i < n:
            while j >= 0:
                if s[j] == "(":
                    print(j)
                    print(res[j])
                    res.pop(j)
                    i += 1
                    j -= 1
                    break
                elif s[j] != "(":
                    j -= 1

            

        
        return str(''.join(res))
            




        