# Happy number
"""
Approach: Compute sum of squares iteratively and store them in a set until the computed sum is either 1 or is present in our set
"""

class Solution:
    def get_square_sum(self, n:int) -> int:
        res = 0
        while n > 0:
            num = n%10
            res += num*num
            n = n//10
            
        return res
    
    def isHappy(self, n: int) -> bool:
        store = set()
        while True:
            
            n = self.get_square_sum(n)
            
            if n == 1:
                return True
            
            if n in store:
                return False
            
            store.add(n)
        
