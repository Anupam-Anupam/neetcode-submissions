class Solution:
    def maxScore(self, s: str) -> int:

        leftsum = []
        rightsum = []
        left = 0
        right = 0
        maxsum = 0

        for char in range(len(s)-1):
            if s[char] == "1":
                leftsum.append(left)
            if s[char] == "0":
                left += 1
                leftsum.append(left)

        for i in range(len(s) - 1, 0, -1):
            if s[i] == "0":
                rightsum.append(right)
            if s[i] == "1":
                right += 1
                rightsum.append(right)

        rightsum.reverse()
        print(leftsum)
        print(rightsum)

        for i in range(len(s)-1):
            maxsum = max(maxsum, leftsum[i] + rightsum[i])

        return maxsum


        