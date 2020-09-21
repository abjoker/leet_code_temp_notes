"""
Approach: use a one-pass hash map which either checks if target-num value is present in hash or inserts the value

Do not repeat yourself
"""
def twoSum(nums: List[int], target: int) -> List[int]:
        hash_map = {}
        for index, num in enumerate(nums):
            if target-num in hash_map and index != hash_map[target-num]:
                return index, hash_map[target-num]
            
            hash_map[num] = index
        
