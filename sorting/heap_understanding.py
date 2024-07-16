from heapq import heapify, heappop
from typing import List
class Solution:
    def heap_sort(self, lst:List[int])->None:
        heapify(lst)
        print('After heapify : ', lst)
        res = []
        while lst:
            res.append(heappop(lst))
            print(lst)
            
        print('Final sort :', res)
    

if __name__ == "__main__":
    obj = Solution()
    input = [5,3,2,1]
    obj.heap_sort(input)