"""
Approach: Use a hash map to store first list where key is word and value is index
For the second list, iterate through all the elements check if it exits in the hash map, if yes
check its sum, if it is equal to the smallest value, append to that list and if it is smaller than
that value then create a new list. Return this list as a result
"""
def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        min_val = float("inf")
        hmap1 = {word: index for index, word in enumerate(list1)}
        lsum = []
        
        for index, word in enumerate(list2):
            
            if word in hmap1:
                check_val = index + hmap1[word]
                
                if check_val < min_val:
                    min_val = check_val
                    lsum = [word]
                elif check_val == min_val:
                    lsum.append(word)
                else:
                    pass
                    

        return lsum
