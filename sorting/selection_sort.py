from typing import List


class Solution:
    def selection_sort(self,lst:List[int])-> None: 
        for i in range(len(lst)):
            min_idx = i
            for j in range(i+1, len(lst)):
                if lst[j]< lst[min_idx]:
                    min_idx = j
            #swap
            lst[min_idx], lst[i] = lst[i], lst[min_idx]
        print(lst)


if __name__ == "__main__":
    obj = Solution()
    input = [7,3,2,5,6,10,9,8,1]
    input_2 = [2,0,2,1,1,0]
    input_3 = [2,0,1]
    obj.selection_sort(input_3)

