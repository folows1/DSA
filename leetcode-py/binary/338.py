from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        list = []
        for i in range(n + 1):
            count = 0
            while i > 0:
              print ('i:', i)
              print('i and 1:', i & 1)
              count += i & 1
              i >>= 1
            list.append(count)
        return list
    
    def countBits2(self, n: int) -> List[int]:
        ans = [0] * (n + 1)
        print('ans:', ans)
        for x in range(1, n + 1):
            print('x:', x)
            print('x & (x - 1):', x & (x - 1))
            ans[x] = ans[x & (x - 1)] + 1
            print('ans:', ans)
        return ans 
    
s = Solution()
# print(s.countBits(5));
print(s.countBits2(5));
