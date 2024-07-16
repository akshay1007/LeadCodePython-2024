from typing import List


class Solution:
    def heightChecker(self,height:List[int])->int:
        count = 0
        sorted_height = sorted(height)
        i = 0 
        while i < len(height) :
            if height[i] != sorted_height[i] :
                count +=1
            i +=1
        return count


if __name__ == "__main__":
    obj = Solution()
    heights = [1,1,4,2,1,3]
    print('Lenght of the list : ', len(heights))
    print(obj.heightChecker(heights))