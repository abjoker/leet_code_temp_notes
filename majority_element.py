"""
First element is termed the majority element
if same element is found count is incremented
else count id decremented
if count is zero then the element encounterd becomes the new majority element

at the end of our iteration, whatever is our majority element is the result
"""
class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        major = float('-inf')
        count = 0
        for _, val in enumerate(nums):
            if count == 0:
                major = val
                count += 1
            elif val == major:
                count += 1
            else:
                count -= 1
        
        return major
