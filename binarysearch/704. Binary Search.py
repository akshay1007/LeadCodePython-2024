class Solution:
    def search(self,nums,target):
        left = 0 
        right = len(nums)-1
        while left <= right :
            mid = (left+right)//2
            if nums[mid]==target:
                return mid
            elif nums[mid] > target :
                right = mid-1
            else :
                left = mid+1
        return -1


if __name__ == '__main__':
    nums = [-1,0,3,5,9,12]
    target = 9
    Output =  4
    
    nums1 = [-1,0,3,5,9,12]
    target1 = 2
    Output1 = -1

    nums2 = [5]
    target2 = 5
    Output2 = 0
    obj = Solution()

    result = obj.search(nums,target)
    print(result==Output)
    result1 = obj.search(nums1,target1) 
    print(result1==Output1)
    result2 = obj.search(nums2,target2) 
    print('Result 2 : ', result2)
    print(result2==Output2)


