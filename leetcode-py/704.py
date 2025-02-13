class Solution:
    def search(self, nums, target) -> int:
        lo = 0
        hi = len(nums)
        while lo < hi:
            mid = int((lo + hi) / 2)

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                lo = mid + 1
            else:
                hi = mid
        return -1
        
        