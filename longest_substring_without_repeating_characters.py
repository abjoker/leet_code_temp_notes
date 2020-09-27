#APPROACH 1: SLIDING WINDOW
def lengthOfLongestSubstring(self, s: str) -> int:
      hash_set = set()
      i = j = res = 0

      while i < len(s) and j < len(s):
          if s[j] not in hash_set:
              hash_set.add(s[j])
              j += 1
              res = max(res, j-i)
          else:
              hash_set.remove(s[i])
              i += 1

      return res

def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = {}
        left = res = 0
        
        for right, val in enumerate(s):
            if val in hash_map and left <= hash_map[val]:
                left = hash_map[val] + 1
            else:
                # +1 since left points to first element of substring and right points to last
                res = max(res, right - left + 1)
                
            hash_map[val] = right
            
        return res
