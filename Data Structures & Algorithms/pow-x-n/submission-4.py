class Solution:
    def myPow(self, x: float, n: int) -> float:

            if n == 0:
                return 1.0

            negative = n < 0
            n = abs(n)

            res = 1.0


            while n>0:
                if n%2 == 1:
                    res *= x

                x *= x

                n //= 2

            
            return (1/res) if negative else res