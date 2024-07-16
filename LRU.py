from collections import OrderedDict
class Solution():
    # LRU Cache
# Get and put
# Capacity
# LRU Eviction

    def __init__(self, capacity:int):
        self.cache =  OrderedDict()
        self.capacity = capacity
    
    def get(self, key:int)-> int :
        if key not in self.cache:
            return -1 
        else:
            self.cache.move_to_end(key)
            return self.cache[key] 
    

    # input (1,1)
    def put(self, key:int, value:int)-> None :
        self.cache[key] = value
        self.cache.move_to_end(key)
        if len(self.cache)> self.capacity:
            self.cache.popitem(last= False)
    
    def lru_print(self):
        print('My cache ', self.cache)
    
if __name__ == "__main__":
    obj = Solution(2)
    obj.put(1,1)
    obj.put(2,2)
    obj.lru_print()
    print('Get elemet : ', obj.get(1))
    obj.lru_print()
    obj.put(3,3)
    obj.lru_print()
    obj.put(4,4)
    obj.lru_print()




    
    
    
    
    
    
    
    
    
    
    
    
    