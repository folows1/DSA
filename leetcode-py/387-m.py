class Solution:
    def firstUniqChar(self, s: str) -> int:
        r = 0
        counter = {}

        while r < len(s):
          if counter.get(s[r]):
             counter[s[r]] += 1
          else:
             counter[s[r]] = 1
          r+=1
        
        for i in range(len(s)):
           print(s[i])
           print(counter[s[i]])
           print(counter)
           if counter[s[i]] == 1:
              return i
          
        return -1
        


firstUniqChar = Solution().firstUniqChar("aabb")

print(firstUniqChar)