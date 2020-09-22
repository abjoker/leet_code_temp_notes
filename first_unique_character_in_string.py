"""
Use hash map to store character and add count
in second scan see if the count is 1, if yes return the index(coz we know all characters will now already be present in hash map)
"""

def firstUniqChar(s: str) -> int:
        hash_map = {}
        
        for index, val in enumerate(s):
            if val in hash_map:
                hash_map[val] += 1
            else:
                hash_map[val] = 1
                
        
        for index, val in enumerate(s):
            if hash_map[val] == 1:
                return index
            
        return -1
