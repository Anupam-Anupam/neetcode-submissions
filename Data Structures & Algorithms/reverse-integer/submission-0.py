class Solution:
    def reverse(self, x: int) -> int:
        negative = x < 0
        
        return 0 if ((y := int(('-' if x < 0 else '') + ''.join(reversed(list(str(abs(x))))))) < -(2**31) or y > ((2 ** 31) - 1)) else y