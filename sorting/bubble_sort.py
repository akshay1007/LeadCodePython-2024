from typing import List
class Solution:
    def bubble_sort(self,lst:List[int])->None:
        has_swapped = True
        while has_swapped:
            has_swapped = False
            for i in range(len(lst)-1):
                if lst[i]>lst[i+1]:
                    #swapped
                    lst[i], lst[i+1] = lst[i+1],lst[i]
                    has_swapped = True
        print('Output : ' , lst)
      


if __name__ == "__main__":
    obj = Solution()
    input = [7,3,2,5,6,10,9,8,1]
    input_2 = [2,0,2,1,1,0]
    input_3 = [2,0,1]
    print('Input' , input)
    obj.bubble_sort(input)
