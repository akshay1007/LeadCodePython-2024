from typing import List
class Solution:
    def rotate(self,lst:List[int], k:int):
        for _ in range(k):
            previous = lst[-1] # initiate the last element
            for i in range(len(lst)):
                temp = lst[i]  # hold the i element
                lst[i] = previous # overwrite the current index
                previous = temp
        print(lst)

    def rotate2(self,lst:List[int], k:int):
        a = [0] * len(lst)
        for i in range(len(lst)):
            a[(i+k)%len(lst)] = lst[i]
            print('i : ', i , 'k : ', k , 'value : ', (i+k)%len(lst), 'updated list : ', a)
    
    def rotate3(self,lst:List[int], k:int):
        k %= len(lst)
        self.reverse(lst,0 , len(lst)-1)
        print(lst)
        self.reverse(lst,0,k-1)
        print(lst)
        self.reverse(lst,k,len(lst)-1)
        print(lst)

    def reverse(self,lst,start,end):
        while start < end :
            temp = lst[start]
            lst[start] = lst[end]
            lst[end] = temp
            start += 1
            end -= 1 

            
        
if __name__ == "__main__":
    obj = Solution()
    input = [1,2,3,4,5,6,7]
    k = 3
    obj.rotate3(input,k)
 

