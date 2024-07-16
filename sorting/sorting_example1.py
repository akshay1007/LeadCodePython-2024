from typing import List


class Solution:
    def sort_by_length(self,lst:List[str])->None:
        lst.sort(key = lambda x: len(x))
        print(lst)
        

 
if __name__=="__main__": 
    obj = Solution()
    input = ["hello", "world", "we", "are", "learning", "sorting"]
    input_2 = ['hello', 'your', 'above', 'year', 'alone', 'friendly', 'crazy']
    obj.sort_by_length(input)
    obj.sort_by_length(input_2)

