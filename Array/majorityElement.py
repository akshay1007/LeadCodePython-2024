from typing import List

class Solution:
    def majorityElement(self,lst:List[int])-> int :
        count = 0 # 1 , 0 
        majority = 0  # 2 

        # Traveser through the list
        for i in range(len(lst)):
            if count == 0 and majority != lst[i]:   
                majority = lst[i] # 2 
                count += 1  # 1
            elif majority == lst[i]:
                count += 1 # 2 , 2  , 3  
            else:
                count -=1 # 1  , 2 , 3 
        return majority



if __name__ == "__main__":
    input = [2,2,1,2,1,1,1,2,2, 3,3,3,3,3,3,3,2,2,2,2,2,2,2,2,2]
    obj = Solution()
    majority_element = obj.majorityElement(input)
    print('Majority element is : ', majority_element)

