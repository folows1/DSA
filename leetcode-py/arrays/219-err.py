from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        l, r = 0, 0
        if k == 0:
            return False
        
        while r - l <= k:
           r += 1
           if l+1 >= len(nums):
               return False
           print('lr', l, r)
           if r - l > k or r == len(nums):
              l += 1
              r = l
              print('reset', l, r)
            
           for i in range(l, r+1):
                print('LR', l, r)
                if nums[i] == nums[l] and i - l <= k and i != l:
                    return True
        return False

s = Solution()
nums = [1,2,3,1,2,3]
k = 2 
# false

# nums = [1, 2, 3, 1]
# k = 3
# true
# nums = [1, 0, 1, 1]
# k = 1
      # 0 1 2 3 4 5 6 7 8 9    
# nums = [1,2,3,4,5,6,7,8,9,9]
# k = 3

print(s.containsNearbyDuplicate(nums, k))