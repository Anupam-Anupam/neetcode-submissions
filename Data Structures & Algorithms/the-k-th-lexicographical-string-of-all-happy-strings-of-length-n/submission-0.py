class Solution:
    def getHappyString(self, n: int, k: int) -> str:
        res = []

        def backtrack():
            if len(res) == k:
                return 

            if len(curr) == n:
                res.append("".join(curr))
                return

            for letter in "abc":
                if curr and curr[-1] == letter:
                    continue
                
                curr.append(letter)
                backtrack()
                curr.pop()

        
        curr = []
        backtrack()
                        

        return res[k-1] if len(res) >= k else ""



                        






