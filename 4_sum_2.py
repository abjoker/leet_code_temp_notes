from collections import Counter
from itertools import product
class Solution:
    def fourSumCount(self, A: List[int], B: List[int], C: List[int], D: List[int]) -> int:
        """
        storing sum of combination of values in A and B
        them storing the counts of each sum encountered
        in a hash map
        
        check if (a+b) = -(c+d)
        
        storing the counts to verify if other such combinations exist
        """
        AB = Counter(a+b for a,b in product(A, B))
        ctr = 0
        for c,d in product(C, D):
            val = -(c+d)
            if val in AB:
                ctr += AB[val]
        
        return ctr 
