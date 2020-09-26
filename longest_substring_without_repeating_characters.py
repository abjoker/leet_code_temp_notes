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
