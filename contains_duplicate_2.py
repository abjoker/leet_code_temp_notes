"""
Use a hash map, if value already exits and condition is satified, return True else return False at the end
"""

def containsNearbyDuplicate(nums: List[int], k: int) -> bool:
        hash_map = {}
        
        for index, val in enumerate(nums):
            if val in hash_map and index - hash_map[val] <= k:
                return True
            else:
                hash_map[val] = index
                
        return False
