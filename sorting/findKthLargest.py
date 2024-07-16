from heapq import heapify, heappop
import heapq
from typing import List

class Solution:
    def findKthLargest(self, lst : List[int], k)->int :
        heapify(lst)
        print (lst)
        el = None
        while len(lst)>k:
            el = heappop(lst)
           
        return el

if __name__=="__main__":
    obj = Solution()
    input = [3,2,1,5,6,4]
    k = 2
    heap = [-n for n in input]
    res = None
    heapq.heapify(heap)
    for i in range(k):
        res = heapq.heappop(heap)
    
    print('Result of heap : ', -res)
    print('Result : ', obj.findKthLargest(input,k))
    nums = [1,1,2,2,2,3]
    nums.sort(reverse=True)
    print('nums :', nums)
    res = sorted(nums, key=nums.count)
    print('res :', res)



    