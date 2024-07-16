from typing import List
class Solution:
   def max_profit(self,lst:List[int])-> int : 
        buy = lst[0]
        profit = 0
        for i in range(1,len(lst)):
            if  lst[i] < buy :
                buy = lst[i]
            elif lst[i] - buy > profit:
                profit =  lst[i] - buy

        return profit

   def max_profit_day(self,lst:List[int])-> int : 
       start = lst[0]
       max_profit = 0 
       for i in range(0, len(lst)):
           if start < lst[i]:
               max_profit += lst[i] - start
           start = lst[i]



if __name__ == "__main__":
    obj = Solution()
    input = [7,1,5,3,6,4]
    print('Max Profit : ',obj.max_profit(input))   
    print('Max profit day : ',obj.max_profit_day(input))