class Solution:
    def jump(self,lst):
        reacheable = 0

        for i in range(len(lst)):
            if reacheable < i :
                return False
            reacheable = max(reacheable,i+lst[i])
        
        return True

    def min_jump(self, lst):
        ans = 0 
        curr_end = 0 
        curr_far = 0
        for i in range(len(lst)-1):
            curr_far = max(curr_far, i+ lst[i])
            if i == curr_end:
                ans += 1
                curr_end = curr_far
        return ans

if __name__ == "__main__":
    obj = Solution()
    input1 = [3,2,1,0,4]
    print('Can Reach last ' , obj.jump(input1))  

    input2 = [2,3,0,1,4]
    print('Can Reach last ' , obj.jump(input2))   

    input3 = [3,2,1,0,4]
    print('Can Reach last at min jump ' , obj.min_jump(input3))  

    input4 = [2,3,0,1,4]
    print('Can Reach last  at min jump  ' , obj.min_jump(input4))   

