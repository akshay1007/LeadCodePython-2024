class Solution:
    def productExceptSelf(self,lst):
        n = len(lst)
        ans = [1] * n

        for i in range(1,n):
            ans[i] = ans[i-1] * lst[i-1]

        rightproduct = 1 

        for i in range(n-1, -1, -1):
            ans[i] = ans[i] * rightproduct
            rightproduct = rightproduct * lst[i]
        
        return ans


if __name__ == "__main__":
    obj = Solution()
    input =  [1,2,3,4]
    print(obj.productExceptSelf(input))

