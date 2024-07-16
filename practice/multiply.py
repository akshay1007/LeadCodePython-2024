import unittest

class Solution:
    
    def multiply_array(self,lst):
        temp_arr = [1]*len(lst)
        print(temp_arr)
        product = 1 
        for i in range(1,len(lst)):
            temp_arr[i] = temp_arr[i-1] * lst[i-1]
        print(temp_arr)

        # multiple last to end 
        for i in range(len(lst)-1,-1, -1):
            temp_arr[i] = temp_arr[i] * product
            product *= lst[i]
        print(temp_arr)

        for i in range(len(lst)):
            lst[i] = temp_arr[i]
        print(lst)

    def merge_sorted_array(self,nums1, m , nums2, n):
        ## compare the element of mth and nth place and put greater element at the end of the nums1
        if n == 0 :
            return
        len1 = len(nums1)
        end_idx = len1-1

        while n>0 and m>0:
            if nums2[n-1] >= nums1[m-1]:
                nums1[end_idx] = nums2[n-1]
                n -= 1 
            else :
                nums1[end_idx] = nums1[m-1]
                m -= 1
            end_idx -= 1

        while n>0 :
            nums1[end_idx] = nums2[n-1]
            n -= 1
            end_idx -= 1 
     
        
        return(nums1)

  
if __name__ == "__main__":
    obj = Solution()
    input = [1,2,3,4]
    obj.multiply_array(input)

    # input for merge sorted array 
    nums1 = [1,2,3,0,0,0]
    m = 3
    nums2 = [2,5,6]
    n = 3
    except_result = [1, 2, 2, 3, 5, 6]
    print('Result of merge sort : ',
           obj.merge_sorted_array(nums1,m,nums2,n) ==  except_result)
