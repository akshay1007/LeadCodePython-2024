from typing import List


class Solution:
    def insertion_sort(self,lst:List[int])->None :
        for i in range(1, len(lst)):
            current_index = i
            while current_index > 0 and lst[current_index-1] > lst[current_index]:
                   # Swap elements that are out of order
                    lst[current_index-1], lst[current_index] = lst[current_index],lst[current_index-1]
                    current_index
        print(lst)

if __name__ == "__main__" :
     obj = Solution()
     input = [7,3,2,5,6,10,9,8,1]
     input_2 = [2,0,2,1,1,0]
     input_3 = [2,0,1]
     print('Input' , input)
     obj.insertion_sort(input)
    