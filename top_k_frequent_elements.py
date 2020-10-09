"""
Use a heap on the element counts of the list
"""
from collections import Counter
import heapq
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        count = Counter(nums)   
        # based on the count_values get the nlargest keys
        return heapq.nlargest(k, count.keys(), key = lambda x: count[x])
