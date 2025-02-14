class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        while n > 0:
            print ('n:', n)
            print('n and 1:', n & 1)
            count += n & 1
            n >>= 1
        return count

s = Solution()
print(s.hammingWeight2(9));