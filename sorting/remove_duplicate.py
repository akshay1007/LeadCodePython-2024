from typing import List
class Solution:
    def remove_duplicate(self,lst:List[int], val:int)->int:
        #initialize variable 
        i =0 
        for j in range(len(lst)):
            if lst[j]!= val:
                lst[i], lst[j] = lst[j], lst[i]
                lst.remove(val)
                i +=1
        print('Updated lst : ',lst)
        return i 

    def remove_dup(self,nums,val):
        print('Length of list1 : ', len(nums))
        nums[:]=[num for num in nums if num != val]
        print(nums)
        print('Length of list : ', len(nums))
if __name__ == "__main__":
    obj = Solution()
    input = [2,3,2,3]
    k = 3
    obj.remove_dup(input,k)